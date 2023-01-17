from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import FloatField, IntegerField, CharField, \
    ImageField, Manager, ForeignKey, CASCADE, JSONField

from shared.django import TimeBaseModel, upload_image_product_url


class ProductManager(Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(count__gt=0)


class Product(TimeBaseModel):
    name = CharField(max_length=255)
    description = RichTextField(max_length=7500)
    count = IntegerField(default=0)
    price = FloatField(default=0,
                       validators=[
                           MaxValueValidator(1000000000.00),
                           MinValueValidator(0)
                       ])
    image = ImageField(upload_to=upload_image_product_url)
    views = IntegerField(default=0)
    category = ForeignKey('orders.SubCategory', CASCADE)
    details = JSONField(verbose_name='details of product')

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        db_table = 'product'
