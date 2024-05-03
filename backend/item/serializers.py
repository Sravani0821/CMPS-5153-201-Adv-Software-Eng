from rest_framework import serializers

from . import models


class StoreItemSerializer(serializers.ModelSerializer):
    seller = serializers.StringRelatedField()

    class Meta:
        model = models.StoreItemModel
        fields = (
            "id",
            "seller",
            "title",
            "description",
            "image",
            "opening_bid",
            "contact",
            "auction_end",
            "created_at",
            "updated_at",
            "is_sold",
        )
        read_only_fields = ("id", "created_at", "updated_at", "is_sold")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation["image"]:
            representation["image"] = "http://127.0.0.1:8000" + representation["image"]
        return representation


class StoreItemBidSerializer(serializers.ModelSerializer):
    bidder = serializers.StringRelatedField()

    class Meta:
        model = models.StoreItemBidModel
        fields = (
            "id",
            "bidder",
            "amount",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class LotteryBasedAuctionSerializer(serializers.ModelSerializer):
    seller = serializers.StringRelatedField()

    class Meta:
        model = models.LotteryBasedAuctionModel
        fields = (
            "id",
            "seller",
            "title",
            "description",
            "image",
            "bid",
            "contact",
            "auction_end",
            "created_at",
            "updated_at",
            "is_sold",
        )
        read_only_fields = ("id", "created_at", "updated_at", "is_sold")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation["image"]:
            representation["image"] = "http://127.0.0.1:8000" + representation["image"]
        return representation


class LotteryBasedAuctionBidSerializer(serializers.ModelSerializer):
    bidder = serializers.StringRelatedField()

    class Meta:
        model = models.LotteryBasedAuctionBidModel
        fields = (
            "id",
            "bidder",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotificationModel
        fields = (
            "id",
            "user",
            "message",
            "is_read",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class StoreItemPurchaseSerializer(serializers.ModelSerializer):
    bidder = serializers.StringRelatedField()
    item = StoreItemSerializer()

    class Meta:
        model = models.StoreItemPurchaseModel
        fields = (
            "id",
            "bidder",
            "item",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class LotteryBasedAuctionPurchaseSerializer(serializers.ModelSerializer):
    bidder = serializers.StringRelatedField()
    item = LotteryBasedAuctionSerializer()

    class Meta:
        model = models.LotteryBasedAuctionPurchaseModel
        fields = (
            "id",
            "bidder",
            "item",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")
