from django.contrib import admin
from django.contrib.admin import ModelAdmin
from rangefilter.filters import DateTimeRangeFilter, DateRangeFilter, NumericRangeFilter

from orders.models import Product, Category, SubCategory, Images


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
    exclude = ()


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = ()


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    exclude = ()


@admin.register(Images)
class ImagesAdmin(ModelAdmin):
    exclude = ()
