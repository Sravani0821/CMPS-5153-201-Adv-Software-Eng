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
