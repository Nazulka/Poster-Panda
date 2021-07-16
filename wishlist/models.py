from django.db import models
from django.db.models.signals import post_save

from django.dispatch import receiver
from django.contrib.auth.models import User

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


@receiver(post_save, sender=User)
def create_or_update_user_wishlist(sender, instance, created, **kwargs):
    """
    Create or update the user wishlist
    """
    if created:
        Wishlist.objects.create(user=instance)
    # Existing users: just save the wishlist
    instance.userwishlist.save()
