from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import FormView

from orders.models import Category
from shared.django.context import total_price_of_products, two_best_products
from users.forms import CustomUserCreationForm
from users.mixins import AuthUserMixin
from users.utils.tokens import account_activation_token


class RegisterView(AuthUserMixin, FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth/register.html'

    def form_valid(self, form):
        user = form.save()
        # to get the domain of the current site
        current_site = get_current_site(self.request)
        mail_subject = f'Activation link for {current_site}'
        message = render_to_string('auth/activation.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['total_price'] = total_price_of_products(self.request)
        context['categories'] = Category.objects.all()
        context['two_best_products'] = two_best_products()
        return context
