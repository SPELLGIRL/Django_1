from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество',
                                           default=0)
    add_datetime = models.DateTimeField(verbose_name='время',
                                        auto_now_add=True)

    @property
    def cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        products = Basket.objects.filter(user=self.user)
        total_quantity = 0
        for item in products:
            total_quantity += item.quantity
        return total_quantity

    @property
    def total_cost(self):
        products = Basket.objects.filter(user=self.user)
        total_cost = 0
        for item in products:
            total_cost += item.cost
        return total_cost
