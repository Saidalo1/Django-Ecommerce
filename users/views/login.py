from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView

from users.forms import AuthLoginForm
from users.mixins import AuthUserMixin


class CustomLoginView(AuthUserMixin, FormView):
    form_class = AuthLoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # email = form.data.get('email')
        # password = form.data.get('password')
        user = authenticate(**form.data.dict())
        login(self.request, user)
        return super().form_valid(form)
