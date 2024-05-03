from django.contrib import admin

from . import models


@admin.register(models.ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "created_at"]
    search_fields = ["name", "email", "subject", "message"]
    ordering = ["-created_at"]
