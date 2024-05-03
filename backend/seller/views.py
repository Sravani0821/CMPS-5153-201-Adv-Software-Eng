from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from item.models import (
    StoreItemModel,
    StoreItemBidModel,
    LotteryBasedAuctionModel,
    LotteryBasedAuctionBidModel,
)
from item.serializers import (
    StoreItemSerializer,
    StoreItemBidSerializer,
    LotteryBasedAuctionSerializer,
    LotteryBasedAuctionBidSerializer,
)

from . import serializers
from . import models


class SellerRegisterView(APIView):

    def post(self, request, format=None):
        try:
            data = request.data
            user, created = User.objects.get_or_create(
                username=data["email"],
                defaults={
                    "email": data["email"],
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                },
            )

            if created:
                user.set_password(data["password"])
                user.save()
            data["user"] = user.id

            seller, created = models.SellerModel.objects.get_or_create(
                user=user,
                defaults={
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "date_of_birth": data["date_of_birth"],
                    "email": data["email"],
                    "phone": data["phone"],
                    "address": data["address"],
                    "city": data["city"],
                    "state": data["state"],
                    "country": data["country"],
                    "zip": data["zip"],
                },
            )
            serializer = serializers.SellerSerializer(seller)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class SellerDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            seller = models.SellerModel.objects.get(user=request.user)
            recent_items = StoreItemModel.objects.filter(seller=seller)[0:5]
            recent_auctions = LotteryBasedAuctionModel.objects.filter(seller=seller)[
                0:5
            ]
            recent_store_item_serializer = StoreItemSerializer(recent_items, many=True)
            recent_lottery_auction_serializer = LotteryBasedAuctionSerializer(
                recent_auctions, many=True
            )
            return Response(
                {
                    "recent_store_items": recent_store_item_serializer.data,
                    "recent_lottery_items": recent_lottery_auction_serializer.data,
                }
            )
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class SellerDashboardStoreView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            seller = models.SellerModel.objects.get(user=request.user)
            items = StoreItemModel.objects.filter(seller=seller)
            serializer = StoreItemSerializer(items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class SellerDashboardLotteryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            seller = models.SellerModel.objects.get(user=request.user)
            auctions = LotteryBasedAuctionModel.objects.filter(seller=seller)
            serializer = LotteryBasedAuctionSerializer(auctions, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )
