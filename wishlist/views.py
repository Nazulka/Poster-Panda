from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile


def add_to_wishlist(request, product_id):
    """ A view to add products to the wishlist and remove from it"""

    product = get_object_or_404(Product, pk=product_id)
    
    if product.wishlist_products.filter(pk=request.user.id).exists():
        product.wishlist_product.remove(request.user)
        messages.success(request, 'Successfully removed the item from \
                         the wishlist!')
    else:
        product.wishlist_product.add(request.user)
        messages.success(request, 'Successfully added the item from \
                         the wishlist! ')

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)

