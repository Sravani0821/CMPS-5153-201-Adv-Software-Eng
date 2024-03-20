# Importing the AppConfig class from the django.apps module.
from django.apps import AppConfig

# Defining a configuration class for the "bidder".
class BidderConfig(AppConfig):
    # default auto-generated primary key field.
    default_auto_field = "django.db.models.BigAutoField"
    name = "bidder"
    verbose_name = "Bidder"
