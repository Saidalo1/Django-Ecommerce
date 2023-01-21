from orders.models import Basket, Product


def total_price_of_products(request):
    total_price = 0  # total price of basket objects
    if request.user.is_authenticated:
        user_basket = Basket.objects.filter(user=request.user)  # find all products of user in basket
        if user_basket.exists():
            for item in user_basket:
                if item.product.sale_percent > 0:
                    total_price += item.total_price_of_products
                    continue
                total_price += item.product.price
    return total_price


def two_best_products():
    return Product.objects.order_by('views', 'count')[:2]
