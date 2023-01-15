from django.urls import path

from orders.views import IndexListView, ProductListView
from orders.views.product import ProductDetailView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("products/", ProductListView.as_view(), name="products"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
]
