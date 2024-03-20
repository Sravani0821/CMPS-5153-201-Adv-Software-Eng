from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Importing serializers for seller and bidder models.
from seller import serializers as seller_serializers
from bidder import serializers as bidder_serializers

# a class-based view for user login.
class LoginView(APIView):

# Define POST method to handle login requests.
    def post(self, request, format=None):
        try:
            # Extracting data from request.
            data = request.data
            # Retrieving user object based on provided email.
            user = User.objects.get(username=data["email"])
            # Checking if provided password matches user's password.
            if user.check_password(data["password"]):
                # Generating new tokens for user.
                refresh = RefreshToken.for_user(user)
# Returning the new tokens in the response.
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    }
                )
            else:
                # Returning unauthorized status if password doesn't match.
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            # Handling any exceptions and returning appropriate response.
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )

# Define a class-based view for user logout.
class LogoutView(APIView):
     # Setting permission classes to allow only authenticated users to access.
    permission_classes = (IsAuthenticated,)
 # Define POST method to handle logout requests.
    def post(self, request, format=None):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            # Returning a successful response indicating logout.
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            # Handling any exceptions and returning appropriate response.
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Define a class-based view for retrieving user details.
class UserView(APIView):
    # Setting permission classes to allow only authenticated users to access this view.
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # check if user is seller or bidder
        user = request.user
        if hasattr(user, "sellermodel"):
            # Serializing seller data if user is a seller.
            serializer = seller_serializers.SellerSerializer(user.sellermodel)
            data = {
                "type": "seller",
                "data": serializer.data,
            }
            # Returning seller data in the response.
            return Response(data)
     # Checking if user is a bidder.
        elif hasattr(user, "biddermodel"):
           # Serializing bidder data if user is a bidder. 
            serializer = bidder_serializers.BidderSerializer(user.biddermodel)
            data = {
                "type": "bidder",
                "data": serializer.data,
            }
            # Returning bidder data in the response.
            return Response(data)
        else:
            # Returning not found status if user is neither seller nor bidder.
            return Response(status=status.HTTP_404_NOT_FOUND)
