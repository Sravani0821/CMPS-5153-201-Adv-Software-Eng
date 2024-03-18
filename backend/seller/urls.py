from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.SellerRegisterView.as_view(), name="seller_register"),
]
