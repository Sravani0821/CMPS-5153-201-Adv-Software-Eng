# Generated by Django 5.0.3 on 2024-03-15 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bidder", "0001_initial"),
        ("seller", "0002_rename_seller_sellermodel"),
    ]

    operations = [
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
    ]
