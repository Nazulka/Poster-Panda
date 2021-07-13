from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile
from wishlist.models import Wishlist, WishlistItem



def add_to_wishlist(request, product_id):
    """ A view to add products to the wishlist and remove from it"""

    user = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist = Wishlist.objects.all()
    # wishlists = user.wishlist.all()
  
    if request.method == 'POST':

        if wishlist.product.filter(pk=request.user.id).exists():
            wishlist.product.remove(request.user)
            
            messages.success(request, 'Successfully removed the item from \
                            the wishlist!')
        else:
            wishlist.product.add(request.user)
            messages.success(request, 'Successfully added the item to the \
                             wishlist! ')
                             
    print(f"WISHLIST: {wishlist}")
    template = 'wishlist/wishlist.html'
    context = {
        'product': product,
        'wishlist': wishlist,
    }

    return render(request, template, context)
