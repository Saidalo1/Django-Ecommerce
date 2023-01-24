from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from users.forms import ProfileModelForm


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'profile'
    form_class = ProfileModelForm
    redirect_authenticated_user = True
    template_name = 'auth/account_settings.html'
    success_url = reverse_lazy("products")

    def get_object(self, queryset=None):
        return self.request.user
