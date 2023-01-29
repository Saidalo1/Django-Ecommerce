from django.forms import ModelForm

from users.models import User


class ProfileModelForm(ModelForm):
    class Meta:
        model = User
        exclude = ("is_active", "date_joined", "is_staff", "email", "password")
