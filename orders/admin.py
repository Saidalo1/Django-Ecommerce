from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm
from django_admin_hstore_widget.forms import HStoreFormField
from rangefilter.filters import DateTimeRangeFilter, DateRangeFilter, NumericRangeFilter

from orders.models import Product, Category, SubCategory, Images, Basket
from shared.django import delete_main_photo, delete_all_photos


class ProductAdminForm(ModelForm):
    details = HStoreFormField()

    class Meta:
        model = Product
        exclude = ()


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    search_fields = ('__all__',)
    readonly_fields = ('views',)
    list_display = ('name', 'price', 'category')
    list_filter = (
        ('created_at', DateRangeFilter), ('updated_at', DateTimeRangeFilter), ('price', NumericRangeFilter),
        ('count', NumericRangeFilter),
        ('views', NumericRangeFilter),
        'category',
    )
    form = ProductAdminForm
    exclude = ()

    def delete_model(self, request, obj):
        object_pk = obj.pk
        delete_main_photo(Product, object_pk)
        delete_all_photos(Images, object_pk)
        super().delete_model(request, obj)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = ()


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    exclude = ()


@admin.register(Images)
class ImagesAdmin(ModelAdmin):
    exclude = ()


@admin.register(Basket)
class BasketAdmin(ModelAdmin):
    exclude = ()
