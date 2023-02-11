from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from orders.utils import DataMixin
from users.mixins import AuthUserMixin


class ForgotPasswordView(DataMixin, SuccessMessageMixin, PasswordResetView):
    template_name = 'auth/forgot_password.html'
    email_template_name = "auth/messages/forgot_password_email.html"
    success_message = 'Password reset instruction message has sent to your email!'
    success_url = reverse_lazy('password_reset')


class ForgotPasswordConfirmView(DataMixin, SuccessMessageMixin, AuthUserMixin, PasswordResetConfirmView):
    template_name = 'auth/forgot_password_confirm.html'
    success_message = 'Password has been changed!'
    success_url = reverse_lazy('login')
