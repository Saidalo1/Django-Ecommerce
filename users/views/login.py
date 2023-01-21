from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView

from orders.models import Category
from shared.django.context import two_best_products
from users.forms import AuthLoginForm
from users.mixins import AuthUserMixin


class CustomLoginView(AuthUserMixin, FormView):
    form_class = AuthLoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = authenticate(**form.data.dict())
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error('password', "Please type the correct password")  # is_active or incorrect password error
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['two_best_products'] = two_best_products()
        return context
