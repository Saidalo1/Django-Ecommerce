from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import FloatField, IntegerField, CharField, \
    ImageField, Manager, ForeignKey, CASCADE, JSONField, TextChoices
from django.contrib.postgres.fields import HStoreField

from shared.django import TimeBaseModel, upload_image_product_url, ChoiceArrayField


class ProductManager(Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(count__gt=0)


class Product(TimeBaseModel):
    class ColorsChoices(TextChoices):
        No_Color = 'No Color', 'No Color'
        Black = 'Black', 'Black'
        Red = 'Red', 'Red'
        Orange = 'Orange', 'Orange'
        Yellow = 'Yellow', 'Yellow'
        Green = 'Green', 'Green'
        Blue = 'Blue', 'Blue'
        Indigo = 'Indigo', 'Indigo'
        Violet = 'Violet', 'Violet'
        White = 'White', 'White'

    name = CharField(max_length=255)
    description = RichTextField(max_length=7500)
    count = IntegerField(default=0)
    price = FloatField(default=0,
                       validators=[
                           MaxValueValidator(1000000000.00),
                           MinValueValidator(0)
                       ])
    color = ChoiceArrayField(CharField(max_length=32, choices=ColorsChoices.choices, default=list))
    image = ImageField(upload_to=upload_image_product_url)
    views = IntegerField(default=0)
    category = ForeignKey('orders.SubCategory', CASCADE)
    details = HStoreField(verbose_name='details of product')

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        db_table = 'product'
