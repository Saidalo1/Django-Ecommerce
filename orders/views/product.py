from django.views.generic import ListView, DetailView

from orders.models import Product, Images


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
        return context


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()  # .values('id', 'name', 'description', 'image', 'price')
    template_name = 'product/products.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products_count'] = Product.objects.count()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product_images = Images.objects.filter(product_id=kwargs['object'].id)
        context['product_images'] = (product_images[:3], product_images[3:])
        context['related_products'] = Product.objects.filter(category=kwargs['object'].category)[:6]
        return context
