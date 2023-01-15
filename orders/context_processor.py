from django.utils.timezone import now

from orders.models import Basket, Sales, Category, SubCategory, Product


def counts(request):
    total_price = 0  # total price of basket objects
    if request.user.is_authenticated:
        user_basket = Basket.objects.filter(user=request.user)  # find all products of user in basket
        count_of_cart_objects = user_basket.count()  # count of all products of user in basket
        for item in user_basket:
            sales = Sales.objects.filter(product=item.product, percent__gt=0, from_date__lt=now(),
                                         to_date__gt=now())  # find sales of this products
            if sales.exists():  # if sales exists
                product_discount = 0  # default value of discount
                if sales.count() > 1:  # if sales are more than 1
                    for thing in sales:
                        product_discount += thing.percent  # find total discount
                product_discount = sales.first().percent  # if sales count is 1
                total_price += item.price - item.price * product_discount / 100
                continue
            total_price += item.product.price
    else:
        count_of_cart_objects = 0
    categories = dict()
    for category in Category.objects.all():
        categories[category.name] = SubCategory.objects.filter(category=category).values_list('name')
    two_best_products = Product.objects.order_by('views', 'count')[:2]
    context = {
        'count_of_cart_objects': count_of_cart_objects,
        'total_price': total_price,
        'categories': categories,
        'two_best_products': two_best_products,
    }
    return context
