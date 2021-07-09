from django.db import models

from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):

    """ Model for maintaining a wishlist """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(
        Product,
        through="WishListItem",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="product_wishlists")
    
    def __str__(self):
        return self.products


class WishListItem(models.Model):

    """ The 'through' model that creates link between products and wishlist."""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product
