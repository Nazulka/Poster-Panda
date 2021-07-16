from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile
from wishlist.models import Wishlist, WishlistItem


@login_required
def view_wishlist(request, product_id):
    # product = get_object_or_404(Product, pk=product_id)
    wishlist_product = WishlistItem.objects.filter(product_id=product_id)

    if request.GET:
        template = 'wishlist/wishlist.html'

    context = {
        # 'wishlists': wishlists,
        'wishlist_product': wishlist_product,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add products to the wishlist and remove from it"""

    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # wishlist_items = WishlistItem.objects.all(product=product, user=user)

  
    if request.method == 'POST':
        wishlist_products = WishlistItem.objects.filter(product_id=product_id)

        if wishlist_products.filter(pk=request.user).exists():
            wishlist_products.remove(request.user)
            
            messages.success(request, 'Successfully removed the item from \
                            the wishlist!')
        else:
            wishlist_product.add(request.user)
            messages.success(request, 'Successfully added the item to the \
                             wishlist!')
                             
    template = 'wishlist/wishlist.html'
    context = {
        'product': product,
        'wishlist_products': wishlist_products,
    }

    return render(request, template, context)
