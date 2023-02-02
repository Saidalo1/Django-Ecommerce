from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from users.views import CustomLoginView, ActivateUserView, AccountUpdateView, RegisterView, ChangePasswordView, \
    ForgotPasswordView, ForgotPasswordConfirmView

urlpatterns = [
    # auth
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),

    # account activation
    path("activate_account/<str:uidb64>/<str:token>", ActivateUserView.as_view(), name='activate_user'),

    # account settings
    path("settings/", AccountUpdateView.as_view(), name="account_settings"),

    # change password
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    # forgot password
    path("forgot-password/", ForgotPasswordView.as_view(), name="password_reset"),
    path("reset-password/<uidb64>/<token>/", ForgotPasswordConfirmView.as_view(), name="password_reset_confirm"),
]
