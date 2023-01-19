from django.views.generic import ListView, DetailView

from orders.models import Product, Images
from shared.django.context import count_of_cart_products, total_price_of_products, category_list, two_best_products


class IndexListView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all().values('id', 'name', 'description', 'image', 'price')[:9]

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        thing = Product.objects.all().values('id', 'name', 'image', 'price')[:16]
        if thing.count() > 7:
            featured_products = ((thing[:4]), (thing[4:8]), (thing[8:12]), (thing[12:16]))
            context['featured_products'] = featured_products
        context['featured_products_count'] = thing.count()
        context['products_count'] = Product.objects.count()
        context['count_of_cart_objects'] = count_of_cart_products(self.request)
        context['total_price'] = total_price_of_products(self.request)
        context['categories'] = category_list()
        context['two_best_products'] = two_best_products()
        return context


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()  # .values('id', 'name', 'description', 'image', 'price')
    template_name = 'product/products.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products_count'] = Product.objects.count()
        context['count_of_cart_objects'] = count_of_cart_products(self.request)
        context['total_price'] = total_price_of_products(self.request)
        context['categories'] = category_list()
        context['two_best_products'] = two_best_products()
        return context

    def get_queryset(self):
        name = self.request.GET.get('name__icontains', None)
        sub_category = self.request.GET.get('subCategory', None)
        object_list = super(ProductListView, self).get_queryset()
        if name and name != '':
            if sub_category and sub_category != '':
                object_list = object_list.filter(name__icontains=name, category=sub_category)
            else:
                object_list = object_list.filter(name__icontains=name)
        elif sub_category and sub_category != '':
            object_list = object_list.filter(category=sub_category)
        return object_list


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product_images = Images.objects.filter(product_id=kwargs['object'].id)
        context['product_images'] = (product_images[:3], product_images[3:])
        context['related_products'] = Product.objects.filter(category=kwargs['object'].category)[:6]
        context['count_of_cart_objects'] = count_of_cart_products(self.request)
        context['total_price'] = total_price_of_products(self.request)
        context['categories'] = category_list()
        context['two_best_products'] = two_best_products()
        return context

# class BasketListView(ListView):
#     model = Basket
#     template_name = 'product/basket.html'
#     context_object_name = 'basket_products'
#
#     def get_queryset(self):
#         return Basket.objects.filter(user=self.request.user).values('id', 'product__image', 'product__details', 'count',
#                                                                     'product__price')
#
#     def get_context_data(self, **kwargs):
#         context = super(BasketListView, self).get_context_data(**kwargs)
#         context['count_of_cart_objects'] = count_of_cart_products(self.request)
#         context['total_price'] = total_price_of_products(self.request)
#         context['categories'] = category_list()
#         context['two_best_products'] = two_best_products()
#         return context
