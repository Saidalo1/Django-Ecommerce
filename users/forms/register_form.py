from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField

from users.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
        field_classes = None

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.data['first_name']
        user.last_name = self.data['last_name']
        user.address = self.data['address']
        user.phone = self.data['phone']
        return super().save(commit)
