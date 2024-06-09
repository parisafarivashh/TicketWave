from django.db import models

from .mixins import ModifiedByMixin


class Cart(ModifiedByMixin):
    user = models.ForeignKey('authorize.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'


class CartItems(ModifiedByMixin):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    chair = models.ForeignKey('Chair', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'cartItem'
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItem'

