from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from users.views import CustomLoginView
from users.views import RegisterView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
]
