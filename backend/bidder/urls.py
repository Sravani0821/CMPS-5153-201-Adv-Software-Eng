
from django.urls import path

from . import views

# Defining URL patterns.
urlpatterns = [
    # Mapping the URL path "register/" to the BidderRegisterView class based view with the name "bidder_register".
    path("register/", views.BidderRegisterView.as_view(), name="bidder_register"),
]
