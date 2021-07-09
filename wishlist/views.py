from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile


def add_to_wishlist(request, product_id):
    """ A view to add products to the wishlist """

    product = get_object_or_404(Product, pk=product_id)

    if product.product_wishlist.filter(id=request.user.id).exists():
        product.product_wishlist.remove(request.user)
        messages.success(request, 'Successfully removed the item from \
                         the wishlist!')
    else:
        product.product_wishlist.add(request.user)
        messages.success(request, 'Successfully added the item from \
                         the wishlist! ')
    return redirect(reverse('product_detail', args=[product.id]))

