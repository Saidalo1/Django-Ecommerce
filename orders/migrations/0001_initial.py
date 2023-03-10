# Generated by Django 4.1.4 on 2023-01-23 11:41

import ckeditor.fields
from django.conf import settings
import django.contrib.postgres.fields.hstore
import django.core.validators
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import orders.models.product_handbook
import shared.django.fields
import shared.django.functions


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(max_length=7500)),
                ('count', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0,
                                            validators=[django.core.validators.MaxValueValidator(1000000000.0),
                                                        django.core.validators.MinValueValidator(0)])),
                ('color', shared.django.fields.ChoiceArrayField(base_field=models.CharField(
                    choices=[('No Color', 'No Color'), ('Black', 'Black'), ('Red', 'Red'), ('Orange', 'Orange'),
                             ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Indigo', 'Indigo'),
                             ('Violet', 'Violet'), ('White', 'White')], default=list, max_length=32), size=None)),
                ('image', models.ImageField(upload_to=shared.django.functions.upload_image_product_url)),
                ('views', models.IntegerField(default=0)),
                ('details', django.contrib.postgres.fields.hstore.HStoreField(verbose_name='details of product')),
                ('sale_percent', models.IntegerField(default=0,
                                                     validators=[django.core.validators.MaxValueValidator(100),
                                                                 django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'db_table': 'product',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.category')),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
                'db_table': 'sub_category',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rating',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.subcategory'),
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('type', models.CharField(choices=[('payme', 'Payme')], max_length=85,
                                          verbose_name=orders.models.product_handbook.Payments.PaymentType)
                 ),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=shared.django.functions.upload_other_images_product_url)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'favourite',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.category')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=500)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent',
                 mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            related_name='children', to='orders.comments')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'basket',
            },
        ),
    ]
