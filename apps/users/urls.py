from django.urls import path

from .views import (
    DeleteAccountView,
    LoginView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetRequestView,
    ProfileView,
    PublicProfileView,
    RegisterView,
)

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/profile/", ProfileView.as_view(), name="profile"),
    # Password reset
    path("auth/password-reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    path("auth/password-reset-confirm/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path("auth/change-password/", PasswordChangeView.as_view(), name="change-password"),
    # Public profile – now using UUID
    path("users/<uuid:uuid>/", PublicProfileView.as_view(), name="public-profile"),
    path("auth/profile/delete/", DeleteAccountView.as_view(), name="delete-account"),
]