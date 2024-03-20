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
        )
        read_only_fields = ("id", "created_at", "updated_at")

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
