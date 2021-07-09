from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product
from profiles.models import UserProfile


def add_to_wishlist(request, id):
    """ A view to add products to the wishlist """

    product = 
