from django.urls import path

from orders.views import IndexListView, ProductListView, ProductDetailView, BasketListView, BasketCreateView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),

    # products
    path("products/", ProductListView.as_view(), name="products"),
    path("products/<int:pk>", ProductDetailView.as_view(), name="product_detail"),

    # basket
    path("basket/", BasketListView.as_view(), name="basket"),
    path("basket/add/<int:pk>", BasketCreateView.as_view(), name="basket_create")
]
