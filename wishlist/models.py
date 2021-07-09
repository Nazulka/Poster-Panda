from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):

    """ Model for maintaining a wishlist """

    user = models.ForeignKey(UserProfile, null=False, blank=False,
                             on_delete=models.CASCADE,
                             related_name='wishlist')
    products = models.ManyToManyField(Product, through='WishlistItem')
    
    def __str__(self):
        return f'Wishlist ({self.user})'


class WishlistItem(models.Model):

    """ The 'through' model that creates link between products and wishlist."""
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='wishlist_products')
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='wishlist_items')

    def __str__(self):
        return self.product.name
