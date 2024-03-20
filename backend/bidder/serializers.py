# Importing necessary modules.
from rest_framework import serializers

from . import models

# Defining a seltizer class for the BidderModel.
class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BidderModel
       # fields
        fields = (
            "id",
            "slug",
            "user",
            "first_name",
            "last_name",
            "email",
            "phone",
        )
        # Specifying read_only_fields in the serialization.
        read_only_fields = ("id", "slug", "user")
