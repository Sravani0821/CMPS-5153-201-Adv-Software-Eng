from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from seller.models import SellerModel
from bidder.models import BidderModel


class StoreItemModel(models.Model):
    seller = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="item_images")
    opening_bid = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=100)
    auction_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        db_table = "item"
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ["-created_at"]


class StoreItemBidModel(models.Model):
    item = models.ForeignKey(StoreItemModel, on_delete=models.CASCADE)
    bidder = models.ForeignKey(BidderModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return (
            self.item.title
            + " - "
            + self.bidder.first_name
            + " "
            + self.bidder.last_name
        )

    def __str__(self):
        return (
            self.item.title
            + " - "
            + self.bidder.first_name
            + " "
            + self.bidder.last_name
        )

    class Meta:
        db_table = "item_bid"
        verbose_name = "Item Bid"
        verbose_name_plural = "Item Bids"
        ordering = ["-created_at"]
