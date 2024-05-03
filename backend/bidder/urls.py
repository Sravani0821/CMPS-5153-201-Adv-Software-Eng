from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.BidderRegisterView.as_view(), name="bidder_register"),
    path("dashboard/", views.BidderDashboardView.as_view(), name="bidder_dashboard"),
]
