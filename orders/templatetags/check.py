from django import template

from orders.models import Basket, Favourite

register = template.Library()


@register.filter
def has_cart(product, user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user, product=product).exists()
    return False


@register.filter
def has_fav(product, user):
    return Favourite.objects.filter(user=user, product=product).exists()
