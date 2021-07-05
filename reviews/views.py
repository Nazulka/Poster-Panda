from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from .models import ProductReview
from .forms import AddReviewForm
from products.models import Product
from profiles.models import UserProfile


# Create your views here.
# def product_reviews(request):
#     """ A view to show all reviews for the product """

#     product_reviews = ProductReview.objects.all().order_by('-date_posted')

#     if request.GET:

#         template = 'reviews/reviews.html'
        
#     context = {
#         'product_reviews': product_reviews,
#     }

#     return render(request, template, context)


@login_required
def add_review(request, product_id):
    """ Add a review to the product """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        review_form = AddReviewForm(
            user=request.user,
            product=request.POST.get('product'),
            review_rating=request.POST('review_rating'),
            review_headline=request.POST.get('review_headline'),
            review_comments=request.POST.get('review_comments'),
        )


        review_form.save()
        messages.success(request, 'Successfully added review!')
        
        return redirect(reverse('product_detail', args=[product.id]))
    
    context = {
        'form': AddReviewForm
    }

    return render(request, 'reviews/add_review.html', context)
