from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile


def add_to_wishlist(request, product_id):
    """ A view to add products to the wishlist and remove from it"""
    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlists = user.wishlist.all()
  
    wishlist = Wishlist.objects.get.all()

    if request.method == 'POST':

        if wishlist.products.filter(pk=request.user.id).exists():
            wishlist.products.remove(request.user)
            messages.success(request, 'Successfully removed the item from \
                            the wishlist!')
        else:
            wishlist.product.add(request.user)
            messages.success(request, 'Successfully added the item from \
                            the wishlist!')

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context)
