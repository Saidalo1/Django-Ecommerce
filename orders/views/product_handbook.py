from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView

from orders.models import Basket, Category
from shared.django.context import two_best_products


class BasketListView(ListView):
    model = Basket
    template_name = 'product/basket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['two_best_products'] = two_best_products()
        return context


class BasketCreateView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        cart, created = Basket.objects.get_or_create(user=self.request.user, product_id=kwargs['pk'])
        if not created:
            cart.delete()
        return redirect(self.request.GET.get('url', 'products'))

    def post(self, *args, **kwargs):
        product_basket_count = self.request.POST.get('product_basket_count')
        Basket.objects.update_or_create(user=self.request.user, product_id=kwargs['pk'],
                                        count=product_basket_count)
        return redirect(self.request.GET.get('url', 'basket'))