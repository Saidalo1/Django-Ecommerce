from django.core.exceptions import ValidationError
from django.forms import Form, EmailField, CharField

from users.models import User


class AuthLoginForm(Form):
    email = EmailField(max_length=255)
    password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("This user didn't registered!")
        return email
