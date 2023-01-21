from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, EmailField
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if User.objects.filter(email=email).exists():
            raise ValueError("This email is already exists")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if User.objects.filter(email=email).exists():
            raise ValueError("This email is already exists")
        user = self.create_user(
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)
        return user


class User(AbstractUser):
    phone = CharField(max_length=12, null=True, blank=True)
    is_active = BooleanField(default=False)
    email = EmailField(_("email address"), unique=True)
    address = CharField(max_length=512)

    USERNAME_FIELD = 'email'

    objects = UserManager()
    REQUIRED_FIELDS = ()

    @property
    def total_price_of_all_products(self):
        total_price = sum(item.total_price_of_products for item in self.basket_set.all())
        return total_price

    def save(self, *args, **kwargs):
        if self.username is None or self.username == '':
            self.username = f'User000{User.objects.count()}'
        super().save(*args, **kwargs)
