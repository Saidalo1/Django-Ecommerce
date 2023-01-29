from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from users.views import CustomLoginView, ActivateUserView, AccountUpdateView, RegisterView, ChangePasswordView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path("activate_account/<str:uidb64>/<str:token>", ActivateUserView.as_view(), name='activate_user'),
    path("settings/", AccountUpdateView.as_view(), name="account_settings"),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]
