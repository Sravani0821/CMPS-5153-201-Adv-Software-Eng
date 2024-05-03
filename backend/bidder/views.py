from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from item.models import (
    StoreItemModel,
    StoreItemBidModel,
    StoreItemPurchaseModel,
    LotteryBasedAuctionModel,
    LotteryBasedAuctionBidModel,
    LotteryBasedAuctionPurchaseModel,
)
from item.serializers import (
    StoreItemSerializer,
    StoreItemBidSerializer,
    StoreItemPurchaseSerializer,
    LotteryBasedAuctionSerializer,
    LotteryBasedAuctionBidSerializer,
    LotteryBasedAuctionPurchaseSerializer,
)

from . import serializers
from . import models


class BidderRegisterView(APIView):

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

            bidder, created = models.BidderModel.objects.get_or_create(
                user=user,
                defaults={
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "email": data["email"],
                    "phone": data["phone"],
                },
            )
            serializer = serializers.BidderSerializer(bidder)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class BidderDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            bidder = models.BidderModel.objects.get(user=request.user)

            # Find store item bids that bidder has bid on
            store_item_bids = StoreItemBidModel.objects.filter(bidder=bidder)

            # Get store items
            store_items = []
            for store_item_bid in store_item_bids:
                if store_item_bid.item not in store_items:
                    store_items.append(store_item_bid.item)

            # Find lottery based auction bids that bidder has bid on
            lottery_based_auction_bids = LotteryBasedAuctionBidModel.objects.filter(
                bidder=bidder
            )

            # Get lottery based auctions
            lottery_based_auctions = []
            for lottery_based_auction_bid in lottery_based_auction_bids:
                if lottery_based_auction_bid.item not in lottery_based_auctions:
                    lottery_based_auctions.append(lottery_based_auction_bid.item)

            store_item_serializer = StoreItemSerializer(store_items, many=True)
            lottery_based_auction_serializer = LotteryBasedAuctionSerializer(
                lottery_based_auctions, many=True
            )

            # Get store item purchases
            store_item_purchases = StoreItemPurchaseModel.objects.filter(bidder=bidder)
            store_item_purchase_serializer = StoreItemPurchaseSerializer(
                store_item_purchases, many=True
            )

            # Get lottery based auction purchases
            lottery_based_auction_purchases = (
                LotteryBasedAuctionPurchaseModel.objects.filter(bidder=bidder)
            )
            lottery_based_auction_purchase_serializer = (
                LotteryBasedAuctionPurchaseSerializer(
                    lottery_based_auction_purchases, many=True
                )
            )

            return Response(
                {
                    "store_items": store_item_serializer.data,
                    "lottery_based_auctions": lottery_based_auction_serializer.data,
                    "store_item_purchases": store_item_purchase_serializer.data,
                    "lottery_based_auction_purchases": lottery_based_auction_purchase_serializer.data,
                }
            )
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )
