from rest_framework import serializers

from . import models


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SellerModel
        fields = (
            "id",
            "slug",
            "user",
            "first_name",
            "last_name",
            "date_of_birth",
            "email",
            "phone",
            "address",
            "city",
            "state",
            "country",
            "zip",
        )
        read_only_fields = ("id", "slug", "user")
