from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from orders.models import Category
from shared.django.context import two_best_products
from users.forms import ProfileModelForm


class AccountUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    context_object_name = 'profile'
    form_class = ProfileModelForm
    template_name = 'auth/account_settings.html'
    success_message = "Your account has been updated successfully"
    success_url = reverse_lazy("account_settings")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(AccountUpdateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['two_best_products'] = two_best_products()
        return context


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'auth/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('change_password')
