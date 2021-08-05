import random
from django.shortcuts import render
from products.models import Product


# Create your views here.

def index(request):
    """ A view to return the index page """

    pool = list(Product.objects.all())
    random.shuffle(pool)

    context = {
        'pool': pool,

    }
    template = 'home/index.html'

    return render(request, template, context)
