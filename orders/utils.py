from django.core.cache import cache

from orders.models import Category, Product


class DataMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get categories from cache
        categories = cache.get('categories')
        if not categories:
            categories = Category.objects.all()
            cache.set('categories', categories, 1800)  # 1800 second

        context['two_best_products'] = Product.objects.order_by('-views', '-count')[:2]
        return context
