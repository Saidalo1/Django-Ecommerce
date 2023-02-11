from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import FormView

from orders.utils import DataMixin
from users.forms import CustomUserCreationForm
from users.mixins import AuthUserMixin
from users.utils.tokens import account_activation_token


class RegisterView(DataMixin, SuccessMessageMixin, AuthUserMixin, FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth/register.html'
    success_message = "Account confirmation link has been sent to your email. Please, confirm your account!"

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
