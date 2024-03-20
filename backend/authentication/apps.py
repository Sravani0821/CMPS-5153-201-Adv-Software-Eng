# Importing the AppConfig class from the django.apps module
from django.apps import AppConfig

# Defining a new configuration class named AuthenticationConfig.
class AuthenticationConfig(AppConfig):
     # Setting the default_auto_field attribute to specify the type of auto-generated primary key field for models.
    default_auto_field = "django.db.models.BigAutoField"
    # Setting the name attribute to specify the full Python path to the application.
    name = "authentication"
