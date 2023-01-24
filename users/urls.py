from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from users.views import CustomLoginView, ActivateUserView, AccountUpdateView
from users.views import RegisterView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path("activate_account/<str:uidb64>/<str:token>", ActivateUserView.as_view(), name='activate_user'),
    path("update/", AccountUpdateView.as_view(), name="account_settings"),
]
