from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from . import serializers
from . import models


class StoreItemListView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            store_items = models.StoreItemModel.objects.all()
            serializer = serializers.StoreItemSerializer(store_items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )


class StoreItemDetailView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            store_item = models.StoreItemModel.objects.get(pk=pk)
            bids = models.StoreItemBidModel.objects.filter(item=store_item)
            item_serializer = serializers.StoreItemSerializer(store_item)
            bid_serializer = serializers.StoreItemBidSerializer(bids, many=True)
            return Response(
                {
                    "item": item_serializer.data,
                    "bids": bid_serializer.data,
                }
            )
        except Exception as e:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": str(e)}
            )
