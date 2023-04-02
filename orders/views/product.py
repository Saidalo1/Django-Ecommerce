from django.db.models import F, Count
from django.views.generic import ListView, DetailView

from orders.models import Product
from orders.utils import DataMixin


class IndexListView(DataMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    queryset = Product.objects.values('id', 'name', 'description', 'image', 'price')[:16]

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        products = Product.objects.annotate(total_sales=Count('order')).order_by('-total_sales').values('id', 'name',
                                                                                                        'price',
                                                                                                        'image')[:16]
        context['featured_products'] = [products[i:i + 4] for i in range(0, 16, 4)]
        return context


class ProductListView(DataMixin, ListView):
    model = Product
    queryset = Product.objects.values('id', 'name', 'description', 'image', 'price')
    template_name = 'product/products.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        # search products
        name = self.request.GET.get('name__icontains', None)
        sub_category = self.request.GET.get('subCategory', None)
        object_list = super(ProductListView, self).get_queryset()
        if name and name != '':
            if sub_category and sub_category != '':
                object_list = object_list.filter(name__icontains=name, category=sub_category)
            else:
                object_list = object_list.filter(name__icontains=name)
        # view products from any category
        elif sub_category and sub_category != '':
            object_list = object_list.filter(category=sub_category)
        return object_list


class ProductDetailView(DataMixin, DetailView):
    model = Product
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        Product.objects.filter(id=kwargs.get('pk')).update(views=F('views') + 1)
        return super().get(request, *args, **kwargs)
