# Importing the path function from the django.urls
from django.urls import path
from . import views
# Defining URL patterns for the application.
urlpatterns = [
    # Mapping the URL path "login/" to the LoginView class-based view with the name "login".
    path("login/", views.LoginView.as_view(), name="login"),
    # Mapping the URL path "logout/" to the LogoutView class-based view with the name "logout".
    path("logout/", views.LogoutView.as_view(), name="logout"),
 # Mapping the URL path "user/" to the UserView class-based view with the name "user".
    path("user/", views.UserView.as_view(), name="user"),
]
