from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.SellerRegisterView.as_view(), name="seller_register"),
    path("dashboard/", views.SellerDashboardView.as_view(), name="seller_dashboard"),
    path(
        "dashboard/store/",
        views.SellerDashboardStoreView.as_view(),
        name="seller_dashboard_store",
    ),
    path(
        "dashboard/lottery/",
        views.SellerDashboardLotteryView.as_view(),
        name="seller_dashboard_lottery",
    ),
]
