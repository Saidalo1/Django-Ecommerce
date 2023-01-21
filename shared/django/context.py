from orders.models import Product


def two_best_products():
    return Product.objects.order_by('views', 'count')[:2]


def split_to_4_parts(lst, sz):
    return [lst[i:i + sz] for i in range(0, len(lst), sz)]
