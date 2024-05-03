from rest_framework import serializers

from . import models


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactModel
        fields = (
            "id",
            "name",
            "email",
            "subject",
            "message",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def create(self, validated_data):
        contact, created = models.ContactModel.objects.get_or_create(
            name=validated_data["name"],
            email=validated_data["email"],
            subject=validated_data["subject"],
            message=validated_data["message"],
        )
        return contact

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.subject = validated_data.get("subject", instance.subject)
        instance.message = validated_data.get("message", instance.message)
        instance.save()
        return instance
