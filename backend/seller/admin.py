from django.contrib import admin

from . import models


@admin.register(models.SellerModel)
class SellerModelAdmin(admin.ModelAdmin):
    list_display = (
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
    search_fields = ("user", "first_name", "last_name", "email", "phone")
