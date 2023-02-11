from orders.models import Category, Product


class DataMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['two_best_products'] = Product.objects.order_by('-views', '-count')[:2]
        return context
