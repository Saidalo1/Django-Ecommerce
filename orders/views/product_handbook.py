from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView

from orders.models import Basket, Category
from shared.django.context import total_price_of_products, two_best_products


class BasketListView(ListView):
    model = Basket
    template_name = 'product/basket.html'

    def get_context_data(self, **kwargs):
        context = super(BasketListView, self).get_context_data(**kwargs)
        context['total_price'] = total_price_of_products(self.request)
        context['categories'] = Category.objects.all()
        context['two_best_products'] = two_best_products()
        return context


class BasketCreateView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        cart, created = Basket.objects.get_or_create(user=self.request.user, product_id=kwargs['pk'])
        if not created:
            cart.delete()
        return redirect(self.request.GET.get('url', 'products'))
