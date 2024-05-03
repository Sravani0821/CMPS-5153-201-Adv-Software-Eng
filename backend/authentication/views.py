from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from seller import serializers as seller_serializers
from bidder import serializers as bidder_serializers


class LoginView(APIView):

    def post(self, request, format=None):
        try:
            data = request.data
            user = User.objects.get(username=data["email"])
            if user.check_password(data["password"]):
                refresh = RefreshToken.for_user(user)

                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                )
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # check if user is seller or bidder
        user = request.user
        if hasattr(user, "sellermodel"):
            serializer = seller_serializers.SellerSerializer(user.sellermodel)
            data = {
                "type": "seller",
                "data": serializer.data,
            }
            return Response(data)
        elif hasattr(user, "biddermodel"):
            serializer = bidder_serializers.BidderSerializer(user.biddermodel)
            data = {
                "type": "bidder",
                "data": serializer.data,
            }
            return Response(data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
