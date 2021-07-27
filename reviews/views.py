from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ProductReview
from .forms import AddReviewForm

from products.models import Product
from profiles.models import UserProfile


# Create your views here.
def product_reviews(request):
    """ A view to show all reviews for the product """

    reviews = ProductReview.objects.all().order_by('-date_posted')
    if request.GET:
        template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }
    return render(request, template, context)


@login_required
def add_review(request, product_id):
    """ Add a product review """

    product = get_object_or_404(Product, pk=product_id)
    user = UserProfile.objects.get(user=request.user)
    user_review = ProductReview.objects.filter(product=product, user=user)
    review_form = AddReviewForm(request.POST)

    if request.method == 'POST':
        if user_review:
            messages.error(request, "You have reviewed this product already.")

        else:
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = user
                review.product = product
                review.save()
                messages.info(request, 'Thank you for your review!')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, "Ensure the form is valid. \
                                    Please try again!")

    else:
        review_form = AddReviewForm(instance=product)

    template = 'reviews/add_review.html'
    context = {
        'review_form': review_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ Save edited product review """

    review = get_object_or_404(ProductReview, pk=review_id)
    if request.user.is_superuser or request.user == review.user:
        if request.method == 'POST':
            review_form = AddReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save()
                messages.info(request, 'Your review has been updated!')
                return redirect(reverse('product_detail',
                                args=[review.product.id]))
            else:
                messages.error(request, 'Failed to update the review. \
                                        Please ensure the form is valid.')
        else:
            review_form = AddReviewForm(instance=review)

        template = 'reviews/edit_review.html',
        context = {
            'review_form': review_form,
            'review': review,
        }
        return render(request, template, context)
    else:
        messages.error(
            request, 'Sorry, only the reviewer can edit this review!')
        return redirect(reverse('product_detail', args=[review.product.id]))


@login_required
def delete_review(request, review_id):
    """ Delete user's existing review """

    review = get_object_or_404(ProductReview, pk=review_id)
    if request.user.is_superuser or request.user == review.user:
        review.delete()
        messages.info(request, 'Your review has been deleted!')
        return redirect(reverse('products'))
    else:
        messages.error(request, 'Sorry, only the reviewer can do that.')
        return redirect(reverse('products'))
