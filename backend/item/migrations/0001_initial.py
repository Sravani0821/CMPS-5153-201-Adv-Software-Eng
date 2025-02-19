# Generated by Django 5.0.3 on 2024-05-02 06:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bidder", "0001_initial"),
        ("seller", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LotteryBasedAuctionModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="item_images")),
                ("bid", models.DecimalField(decimal_places=2, max_digits=10)),
                ("contact", models.CharField(max_length=100)),
                ("auction_end", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_sold", models.BooleanField(default=False)),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="seller.sellermodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lottery Based Auction",
                "verbose_name_plural": "Lottery Based Auctions",
                "db_table": "lottery_based_auction",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="LotteryBasedAuctionBidModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bidder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bidder.biddermodel",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="item.lotterybasedauctionmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lottery Based Auction Bid",
                "verbose_name_plural": "Lottery Based Auction Bids",
                "db_table": "lottery_based_auction_bid",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="LotteryBasedAuctionPurchaseModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bidder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bidder.biddermodel",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="item.lotterybasedauctionmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lottery Based Auction Purchase",
                "verbose_name_plural": "Lottery Based Auction Purchases",
                "db_table": "lottery_based_auction_purchase",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="LotteryBasedAuctionWishlistModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bidder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bidder.biddermodel",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="item.lotterybasedauctionmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Lottery Based Auction Wishlist",
                "verbose_name_plural": "Lottery Based Auction Wishlists",
                "db_table": "lottery_based_auction_wishlist",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="NotificationModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.TextField()),
                ("is_read", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Notification",
                "verbose_name_plural": "Notifications",
                "db_table": "notification",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="StoreItemModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="item_images")),
                ("opening_bid", models.DecimalField(decimal_places=2, max_digits=10)),
                ("contact", models.CharField(max_length=100)),
                ("auction_end", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_sold", models.BooleanField(default=False)),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="seller.sellermodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Items",
                "db_table": "item",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="StoreItemBidModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bidder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bidder.biddermodel",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="item.storeitemmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Item Bid",
                "verbose_name_plural": "Item Bids",
                "db_table": "item_bid",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="StoreItemPurchaseModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bidder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bidder.biddermodel",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="item.storeitemmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Store Item Purchase",
                "verbose_name_plural": "Store Item Purchases",
                "db_table": "store_item_purchase",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="StoreItemWishlistModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "bidder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bidder.biddermodel",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="item.storeitemmodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Item Wishlist",
                "verbose_name_plural": "Item Wishlists",
                "db_table": "item_wishlist",
                "ordering": ["-created_at"],
            },
        ),
    ]
