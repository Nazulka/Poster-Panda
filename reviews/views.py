from django.shortcuts import render

# Create your views here.
def product_reviews(request):
    """ A view to show reviews for the product """

    return render(request, 'reviews/includes/reviews.html')