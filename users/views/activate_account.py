from django.shortcuts import render
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import View

from orders.utils import DataMixin
from users.mixins import AuthUserMixin
from users.models import User
from users.utils.tokens import account_activation_token


class ActivateUserView(DataMixin, AuthUserMixin, View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'auth/login.html',
                          {"msg": {"Account confirmation": "Thank you for your email confirmation. Now you "
                                                           "can login your account"}})
        return render(request, 'auth/login.html',
                      {"msg": {"Account confirmation": "Link is invalid"}})
