# Importing the admin module from Django.
from django.contrib import admin

from . import models

# Registering the BidderModel with the admin site.
@admin.register(models.BidderModel)
class BidderModelAdmin(admin.ModelAdmin):
    # the fields to be displayed in the list view of the admin site.
    list_display = (
        "user",
        "first_name",
        "last_name",
        "email",
        "phone",
    )
    # Defining fields to be searchable in the admin site.
    search_fields = ("user", "first_name", "last_name", "email", "phone")
