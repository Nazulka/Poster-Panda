from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ProductReview
from .forms import AddReviewForm


# Create your views here.
def product_reviews(request):
    """ A view to show all reviews for the product """

    product_reviews = ProductReview.objects.all().order_by('-date_posted')
    template = 'reviews/includes/reviews.html'
    context = {
        'product_reviews': product_reviews,
    }

    return render(request, template, context)


@login_required
def add_review(request):

    """ Add a review to the product """

    if request.method == 'POST':
        form = AddReviewForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')
    else:
        form = AddReviewForm()
        
    template = 'reviews/add_reviews.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


