from django.urls import path

from . import views


urlpatterns = [
    path("store/", views.StoreItemListView.as_view(), name="store_item_list"),
    path("store/new/", views.StoreItemCreateView.as_view(), name="store_item_create"),
    path(
        "store/<int:pk>/", views.StoreItemDetailView.as_view(), name="store_item_detail"
    ),
    path("store/<int:pk>/bid/", views.BidCreateView.as_view(), name="bid_create"),
    path(
        "store/<int:pk>/accept/",
        views.BidderAcceptStoreItemView.as_view(),
        name="bidder_accept",
    ),
    path(
        "store/<int:pk>/reject/",
        views.BidderRejectStoreItemView.as_view(),
        name="bidder_reject",
    ),
    path(
        "store/<int:pk>/wishlist/",
        views.StoreItemWishlistView.as_view(),
        name="store_item_wishlist",
    ),
    path(
        "store/<int:pk>/sell/",
        views.StoreItemSellView.as_view(),
        name="store_item_sell",
    ),
    #
    path("lottery/", views.LotteryBasedAuctionListView.as_view(), name="lottery_list"),
    path(
        "lottery/new/",
        views.LotteryBasedAuctionCreateView.as_view(),
        name="lottery_create",
    ),
    path(
        "lottery/<int:pk>/",
        views.LotteryBasedAuctionDetailView.as_view(),
        name="lottery_detail",
    ),
    path(
        "lottery/<int:pk>/bid/",
        views.LotteryBasedAuctionBidView.as_view(),
        name="lottery_bid",
    ),
    path(
        "lottery/<int:pk>/accept/",
        views.LotteryBasedAuctionAcceptView.as_view(),
        name="lottery_accept",
    ),
    path(
        "lottery/<int:pk>/reject/",
        views.LotteryBasedAuctionRejectView.as_view(),
        name="lottery_reject",
    ),
    path(
        "lottery/<int:pk>/wishlist/",
        views.LotteryBasedAuctionWishlistView.as_view(),
        name="lottery_wishlist",
    ),
    path(
        "lottery/<int:pk>/draw/",
        views.LotteryBasedAuctionDrawView.as_view(),
        name="lottery_draw",
    ),
    #
    path(
        "notifications/", views.NotificationListView.as_view(), name="notification_list"
    ),
    path(
        "notifications/count/",
        views.NotificationCountView.as_view(),
        name="notification_count",
    ),
]
