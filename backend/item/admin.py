from django.contrib import admin

from . import models


@admin.register(models.StoreItemModel)
class StoreItemModelAdmin(admin.ModelAdmin):
    list_display = (
        "seller",
        "title",
        "description",
        "image",
        "opening_bid",
        "contact",
        "auction_end",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "seller",
        "title",
        "description",
        "image",
        "opening_bid",
        "contact",
        "auction_end",
    )


@admin.register(models.StoreItemBidModel)
class StoreItemBidModelAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "bidder",
        "amount",
        "created_at",
    )
    search_fields = (
        "item",
        "bidder",
        "amount",
    )


@admin.register(models.LotteryBasedAuctionModel)
class LotteryBasedAuctionModelAdmin(admin.ModelAdmin):
    list_display = (
        "seller",
        "title",
        "description",
        "image",
        "bid",
        "contact",
        "auction_end",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "seller",
        "title",
        "description",
        "image",
        "bid",
        "contact",
        "auction_end",
    )


@admin.register(models.LotteryBasedAuctionBidModel)
class LotteryBasedAuctionBidModelAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "bidder",
        "created_at",
    )
    search_fields = (
        "item",
        "bidder",
    )


@admin.register(models.StoreItemWishlistModel)
class StoreItemWishlistModelAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "bidder",
        "created_at",
    )
    search_fields = (
        "item",
        "bidder",
    )


@admin.register(models.LotteryBasedAuctionWishlistModel)
class LotteryBasedAuctionWishlistModelAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "bidder",
        "created_at",
    )
    search_fields = (
        "item",
        "bidder",
    )


@admin.register(models.NotificationModel)
class NotificationModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "message",
        "created_at",
    )
    search_fields = (
        "user",
        "message",
    )


@admin.register(models.StoreItemPurchaseModel)
class StoreItemPurchaseModelAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "bidder",
        "created_at",
    )
    search_fields = (
        "item",
        "bidder",
    )


@admin.register(models.LotteryBasedAuctionPurchaseModel)
class LotteryBasedAuctionPurchaseModelAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "bidder",
        "created_at",
    )
    search_fields = (
        "item",
        "bidder",
    )
