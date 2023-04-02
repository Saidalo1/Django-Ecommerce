from django.db.models import CASCADE, ForeignKey, Model, CharField, ImageField, \
    FloatField, IntegerField, TextField, TextChoices
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.django import TimeBaseModel, upload_other_images_product_url
from users.models import User


class Category(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name_plural = "Categories"


class SubCategory(Model):
    name = CharField(max_length=50)
    category = ForeignKey(Category, CASCADE)

    def __str__(self):
        return f'{self.category.name} --> {self.name}'

    class Meta:
        db_table = 'sub_category'
        verbose_name_plural = "Sub Categories"


class Company(Model):
    name = CharField(max_length=200)
    type = ForeignKey(Category, CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company'


class Images(Model):
    product = ForeignKey('orders.Product', CASCADE)
    image = ImageField(upload_to=upload_other_images_product_url)

    class Meta:
        db_table = 'images'
        verbose_name_plural = 'Images'


class Rating(Model):
    product = ForeignKey('orders.Product', CASCADE)
    rating = IntegerField(default=0)
    user = ForeignKey(User, CASCADE)

    def __str__(self):
        return f"{self.rating} {self.product}"

    class Meta:
        db_table = 'rating'


class Comments(TimeBaseModel, MPTTModel):
    product = ForeignKey('orders.Product', CASCADE)
    title = CharField(max_length=255)
    text = TextField(max_length=500)
    user = ForeignKey(User, CASCADE)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.title} {self.product}"

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'comments'


class Basket(Model):
    product = ForeignKey('orders.Product', CASCADE, db_index=True)
    user = ForeignKey(User, CASCADE, db_index=True)
    count = IntegerField(default=1)

    def __str__(self):
        return f"{self.user} {self.count}"

    @property
    def total_price_of_products(self):
        return self.product.total_price * self.count

    class Meta:
        db_table = 'basket'


class Order(Model):
    class Status(TextChoices):
        ordered = 'ordered'
        paid = 'paid'
        delivered = 'delivered'
        received = 'received'

    user = ForeignKey(User, on_delete=CASCADE)
    count = IntegerField(default=0)
    status = IntegerField(default=0)
    product = ForeignKey('orders.Product', CASCADE)

    def __str__(self):
        return f"{self.user} {self.product} {self.count} {self.status}"

    class Meta:
        db_table = 'order'


class Payments(Model):
    class PaymentType(TextChoices):
        payme = 'payme'

    user = ForeignKey(User, on_delete=CASCADE)
    amount = FloatField(default=0)
    type = CharField(PaymentType, max_length=85, choices=PaymentType.choices)

    def __str__(self):
        return f"{self.user} {self.amount}"

    class Meta:
        db_table = 'payments'


class Favourite(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    product = ForeignKey('orders.Product', CASCADE)

    class Meta:
        db_table = 'favourite'
