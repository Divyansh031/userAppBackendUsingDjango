from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    WelcomeView, UserListCreateView, UserDetailView, CustomTokenObtainPairView
)

urlpatterns = [
    path("welcome/", WelcomeView.as_view(), name="welcome"),
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),

    # JWT Token URLs
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
