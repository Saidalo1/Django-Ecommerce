from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView

from orders.models import Basket
from orders.utils import DataMixin


class BasketListView(DataMixin, ListView):
    model = Basket
    template_name = 'product/basket.html'


class BasketCreateView(DataMixin, LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        cart, created = Basket.objects.get_or_create(user=self.request.user, product_id=kwargs['pk'])
        if not created:
            cart.delete()
        current_url = self.request.headers.get('Referer') if self.request.headers.get('Referer') else 'basket'
        return redirect(current_url)

    def post(self, *args, **kwargs):
        product_count = self.request.POST.get('product_basket_count')
        product_basket_count = product_count if product_count and product_count.isdigit() else 1
        Basket.objects.update_or_create(user=self.request.user, product_id=kwargs['pk'],
                                        count=product_basket_count)
        current_url = self.request.headers.get('Referer') if self.request.headers.get('Referer') else 'products'
        return redirect(current_url)
