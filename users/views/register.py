from django.urls import reverse_lazy
from django.views.generic import FormView

from users.forms import CustomUserCreationForm
from users.mixins import AuthUserMixin


class RegisterView(AuthUserMixin, FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
