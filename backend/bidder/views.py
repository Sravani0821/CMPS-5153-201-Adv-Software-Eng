# importing libraries
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
# Importing serializers and models from the current app.
from . import serializers
from . import models

# class based view for registering a bidder.
class BidderRegisterView(APIView):
# Post method to handle registration requests.
    def post(self, request, format=None):
        try:
            # Extracting data from request.
            data = request.data
            # Creating a user object .
            user, created = User.objects.get_or_create(
                username=data["email"],
                defaults={
                    "email": data["email"],
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                },
            )
# If user is newly created, setting password and saving.
            if created:
                user.set_password(data["password"])
                user.save()
            data["user"] = user.id

            bidder, created = models.BidderModel.objects.get_or_create(
                user=user,
                defaults={
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "email": data["email"],
                    "phone": data["phone"],
                },
            )
            # Serializing the bidder object.
            serializer = serializers.BidderSerializer(bidder)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )
