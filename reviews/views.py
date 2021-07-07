from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    user = UserProfile.objects.get(user=request.user)
    review = ProductReview.objects.create(product=product, user=user,
                                            rating=rating,
                                            headline=headline,
                                            comments=comments)
    if request.method == 'POST':
        review_form = AddReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = user
            review.product = product
            review.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, "Ensure the form is valid. \
                                Please try again!")
   
    else:
        review_form = AddReviewForm(instance=product)
      
    context = {
        'review_form': review_form,
        'product': product
    }
    template = 'reviews/add_review.html'

    return render(request, template, context)
