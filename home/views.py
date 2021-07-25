import random
from django.shortcuts import render
from products.models import Product
from profiles.models import UserProfile

from wishlist.models import Wishlist, WishlistItem



# Create your views here.


def index(request):
    """ A view to return the index page """

    # products = Product.objects.all()
    pool = list(Product.objects.all())
    user = UserProfile.objects.get(user=request.user)
    wishlist = Wishlist.objects.get(user=user)
    wishlist_products = WishlistItem.objects.filter(wishlist=wishlist)
    random.shuffle(pool)

    context = {
        # 'products': products,
        'pool': pool,
        'wishlist_products': wishlist_products,

    }
    template = 'home/index.html'

    return render(request, template, context)
