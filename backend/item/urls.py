from django.urls import path

from . import views


urlpatterns = [
    path("store/", views.StoreItemListView.as_view(), name="store_item_list"),
    path("store/<int:pk>/", views.StoreItemDetailView.as_view(), name="store_item_detail"),
]
