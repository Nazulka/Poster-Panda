from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from products.models import Product
from profiles.models import UserProfile
from wishlist.models import Wishlist, WishlistItem


@login_required
def view_wishlist(request):

    user = UserProfile.objects.get(user=request.user)
    wishlist = Wishlist.objects.get(user=user)
    wishlist_products = WishlistItem.objects.filter(wishlist=wishlist)

    context = {
        'wishlist_products': wishlist_products,
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add products to the wishlist and remove from it"""

    if request.method == 'GET':
        # get the wishlist
        user = UserProfile.objects.get(user=request.user)
        wishlist = Wishlist.objects.get(user=user)

        # create a new wishlist item
        product = get_object_or_404(Product, pk=product_id)
        item = WishlistItem.objects.create(product=product, wishlist=wishlist)

    return redirect(reverse('view_wishlist'))
