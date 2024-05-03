from rest_framework import serializers

from . import models


class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BidderModel
        fields = (
            "id",
            "slug",
            "user",
            "first_name",
            "last_name",
            "email",
            "phone",
        )
        read_only_fields = ("id", "slug", "user")
