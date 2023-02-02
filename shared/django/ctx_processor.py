from orders.models import Category, Product


def product_category(request):
    context = {'categories': Category.objects.all(),
               'two_best_products': Product.objects.order_by('views', 'count')[:2]}
    return context
