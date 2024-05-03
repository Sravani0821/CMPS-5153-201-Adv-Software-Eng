from django.contrib import admin

from . import models


@admin.register(models.BidderModel)
class BidderModelAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "first_name",
        "last_name",
        "email",
        "phone",
    )
    search_fields = ("user", "first_name", "last_name", "email", "phone")
