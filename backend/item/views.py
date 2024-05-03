from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth.models import User

from bidder.models import BidderModel
from . import serializers
from . import models


class StoreItemListView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            store_items = models.StoreItemModel.objects.filter(is_sold=False)
            serializer = serializers.StoreItemSerializer(store_items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class StoreItemCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        try:
            seller = models.SellerModel.objects.get(user=request.user)
            store_item, created = models.StoreItemModel.objects.get_or_create(
                seller=seller,
                title=request.data["title"],
                description=request.data["description"],
                image=request.data["image"],
                opening_bid=request.data["opening_bid"],
                contact=request.data["contact"],
                auction_end=request.data["auction_end"],
            )
            serializer = serializers.StoreItemSerializer(store_item)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class StoreItemDetailView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            store_item = models.StoreItemModel.objects.get(pk=pk)
            bids = models.StoreItemBidModel.objects.filter(item=store_item).order_by(
                "-amount", "-created_at"
            )
            item_serializer = serializers.StoreItemSerializer(store_item)
            bid_serializer = serializers.StoreItemBidSerializer(bids, many=True)
            return Response(
                {
                    "item": item_serializer.data,
                    "bids": bid_serializer.data,
                }
            )
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class BidCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        try:
            store_item = models.StoreItemModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            bid = models.StoreItemBidModel.objects.get_or_create(
                item=store_item, bidder=bidder, amount=request.data["amount"]
            )

            # Notify the seller
            seller = store_item.seller
            notification = models.NotificationModel.objects.create(
                user=seller.user,
                message=f"New bid of {request.data['amount']} on {store_item.title}",
            )

            # Notify the wishlist bidders
            wishlist_bidders = models.StoreItemWishlistModel.objects.filter(
                item=store_item
            )
            for wishlist_bidder in wishlist_bidders:
                notification = models.NotificationModel.objects.create(
                    user=wishlist_bidder.bidder.user,
                    message=f"New bid of {request.data['amount']} on {store_item.title}",
                )

            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LotteryBasedAuctionListView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            lottery_items = models.LotteryBasedAuctionModel.objects.filter(
                is_sold=False
            )
            serializer = serializers.LotteryBasedAuctionSerializer(
                lottery_items, many=True
            )
            return Response(serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LotteryBasedAuctionCreateView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        try:
            seller = models.SellerModel.objects.get(user=request.user)
            lottery_item, created = (
                models.LotteryBasedAuctionModel.objects.get_or_create(
                    seller=seller,
                    title=request.data["title"],
                    description=request.data["description"],
                    image=request.data["image"],
                    bid=request.data["bid"],
                    contact=request.data["contact"],
                    auction_end=request.data["auction_end"],
                )
            )
            serializer = serializers.LotteryBasedAuctionSerializer(lottery_item)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LotteryBasedAuctionDetailView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            lottery_item = models.LotteryBasedAuctionModel.objects.get(pk=pk)
            bids = models.LotteryBasedAuctionBidModel.objects.filter(
                item=lottery_item
            ).order_by("-created_at")
            user_bid = models.LotteryBasedAuctionBidModel.objects.filter(
                item=lottery_item, bidder__user=request.user
            ).exists()
            item_serializer = serializers.LotteryBasedAuctionSerializer(lottery_item)
            bid_serializer = serializers.LotteryBasedAuctionBidSerializer(
                bids, many=True
            )
            return Response(
                {
                    "item": item_serializer.data,
                    "bids": bid_serializer.data,
                    "user_bid": user_bid,
                }
            )
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LotteryBasedAuctionBidView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        try:
            lottery_item = models.LotteryBasedAuctionModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            bid = models.LotteryBasedAuctionBidModel.objects.get_or_create(
                item=lottery_item,
                bidder=bidder,
            )

            # Notify the seller
            seller = lottery_item.seller
            notification = models.NotificationModel.objects.create(
                user=seller.user,
                message=f"New bid on {lottery_item.title}",
            )

            # Notify the wishlist bidders
            wishlist_bidders = models.LotteryBasedAuctionWishlistModel.objects.filter(
                item=lottery_item
            )
            for wishlist_bidder in wishlist_bidders:
                notification = models.NotificationModel.objects.create(
                    user=wishlist_bidder.bidder.user,
                    message=f"New bid on {lottery_item.title}",
                )

            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class StoreItemWishlistView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            store_item = models.StoreItemModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            # return true or false
            wishlist_item = models.StoreItemWishlistModel.objects.filter(
                item=store_item, bidder=bidder
            ).exists()
            return Response(wishlist_item)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )

    def post(self, request, pk, format=None):
        try:
            store_item = models.StoreItemModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            wishlist_item = models.StoreItemWishlistModel.objects.get_or_create(
                item=store_item, bidder=bidder
            )
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LotteryBasedAuctionWishlistView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            lottery_item = models.LotteryBasedAuctionModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            # return true or false
            wishlist_item = models.LotteryBasedAuctionWishlistModel.objects.filter(
                item=lottery_item, bidder=bidder
            ).exists()
            return Response(wishlist_item)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )

    def post(self, request, pk, format=None):
        try:
            lottery_item = models.LotteryBasedAuctionModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            wishlist_item = (
                models.LotteryBasedAuctionWishlistModel.objects.get_or_create(
                    item=lottery_item, bidder=bidder
                )
            )
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class NotificationListView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            notifications = models.NotificationModel.objects.filter(
                user=request.user
            ).order_by("-created_at")
            serializer = serializers.NotificationSerializer(notifications, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class NotificationCountView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            count = models.NotificationModel.objects.filter(
                user=request.user, is_read=False
            ).count()
            return Response(count)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class StoreItemSellView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        try:
            store_item = models.StoreItemModel.objects.get(pk=pk)
            store_item.is_sold = True
            store_item.save()

            # Notify the seller
            seller = store_item.seller
            notification = models.NotificationModel.objects.create(
                user=seller.user, message=f"{store_item.title} has been sold"
            )

            # Notify the wishlist bidders
            wishlist_bidders = models.StoreItemWishlistModel.objects.filter(
                item=store_item
            )
            for wishlist_bidder in wishlist_bidders:
                notification = models.NotificationModel.objects.create(
                    user=wishlist_bidder.bidder.user,
                    message=f"{store_item.title} has been sold",
                )

            # Notify the highest bidder to pay
            highest_bid = models.StoreItemBidModel.objects.filter(
                item=store_item
            ).order_by("-amount")[0]
            notification = models.NotificationModel.objects.create(
                user=highest_bid.bidder.user,
                message=f"Please pay for {store_item.title}",
            )

            # create purchase record
            purchase = models.StoreItemPurchaseModel.objects.create(
                item=store_item, bidder=highest_bid.bidder
            )

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LotteryBasedAuctionDrawView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        try:
            lottery_item = models.LotteryBasedAuctionModel.objects.get(pk=pk)
            bidders = models.LotteryBasedAuctionBidModel.objects.filter(
                item=lottery_item
            )
            if bidders:
                import random

                winner = random.choice(bidders)
                notification = models.NotificationModel.objects.create(
                    user=winner.bidder.user,
                    message=f"Congratulations! You have won {lottery_item.title}",
                )
                lottery_item.is_sold = True
                lottery_item.save()

                # Notify the seller
                seller = lottery_item.seller
                notification = models.NotificationModel.objects.create(
                    user=seller.user, message=f"{lottery_item.title} has been sold"
                )

                # Notify the wishlist bidders
                wishlist_bidders = (
                    models.LotteryBasedAuctionWishlistModel.objects.filter(
                        item=lottery_item
                    )
                )
                for wishlist_bidder in wishlist_bidders:
                    notification = models.NotificationModel.objects.create(
                        user=wishlist_bidder.bidder.user,
                        message=f"{lottery_item.title} has been sold",
                    )

                # create purchase record
                purchase = models.LotteryBasedAuctionPurchaseModel.objects.create(
                    item=lottery_item, bidder=winner.bidder
                )

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data={"error": "No bidders"}
                )
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class BidderAcceptStoreItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        try:
            store_item = models.StoreItemModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            purchase = models.StoreItemPurchaseModel.objects.get(
                item=store_item, bidder=bidder
            )

            # Delete purchase record
            purchase.delete()

            # Notify the seller
            seller = store_item.seller
            notification = models.NotificationModel.objects.create(
                user=seller.user, message=f"{store_item.title} has been accepted"
            )

            # Notify the bidder
            notification = models.NotificationModel.objects.create(
                user=bidder.user, message=f"{store_item.title} has been accepted"
            )

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class BidderRejectStoreItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        try:
            store_item = models.StoreItemModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            purchase = models.StoreItemPurchaseModel.objects.get(
                item=store_item, bidder=bidder
            )

            # Delete purchase record
            purchase.delete()

            # Sell to next highest bidder
            highest_bid = models.StoreItemBidModel.objects.filter(
                item=store_item
            ).order_by("-amount")[1]
            purchase = models.StoreItemPurchaseModel.objects.create(
                item=store_item, bidder=highest_bid.bidder
            )

            # Notify the seller
            seller = store_item.seller
            notification = models.NotificationModel.objects.create(
                user=seller.user,
                message=f"{store_item.title} has been offered to next highest bidder",
            )

            # Notify the bidder
            notification = models.NotificationModel.objects.create(
                user=highest_bid.bidder.user,
                message=f"{store_item.title} has been offered to you",
            )

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LotteryBasedAuctionAcceptView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        try:
            lottery_item = models.LotteryBasedAuctionModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            purchase = models.LotteryBasedAuctionPurchaseModel.objects.get(
                item=lottery_item, bidder=bidder
            )

            # Delete purchase record
            purchase.delete()

            # Notify the seller
            seller = lottery_item.seller
            notification = models.NotificationModel.objects.create(
                user=seller.user, message=f"{lottery_item.title} has been accepted"
            )

            # Notify the bidder
            notification = models.NotificationModel.objects.create(
                user=bidder.user, message=f"{lottery_item.title} has been accepted"
            )

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LotteryBasedAuctionRejectView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, format=None):
        try:
            lottery_item = models.LotteryBasedAuctionModel.objects.get(pk=pk)
            bidder = BidderModel.objects.get(user=request.user)
            purchase = models.LotteryBasedAuctionPurchaseModel.objects.get(
                item=lottery_item, bidder=bidder
            )

            # Delete purchase record
            purchase.delete()

            # Draw again, exclude the rejected bidder
            bidders = models.LotteryBasedAuctionBidModel.objects.filter(
                item=lottery_item
            ).exclude(bidder=bidder)

            if bidders:
                import random

                winner = random.choice(bidders)
                notification = models.NotificationModel.objects.create(
                    user=winner.bidder.user,
                    message=f"Congratulations! You have won {lottery_item.title}",
                )
                lottery_item.is_sold = True
                lottery_item.save()

                # Notify the seller
                seller = lottery_item.seller
                notification = models.NotificationModel.objects.create(
                    user=seller.user, message=f"{lottery_item.title} has been sold"
                )

                # Notify the wishlist bidders
                wishlist_bidders = (
                    models.LotteryBasedAuctionWishlistModel.objects.filter(
                        item=lottery_item
                    )
                )
                for wishlist_bidder in wishlist_bidders:
                    notification = models.NotificationModel.objects.create(
                        user=wishlist_bidder.bidder.user,
                        message=f"{lottery_item.title} has been sold",
                    )

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data={"error": "No bidders"}
                )
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )
