from django.shortcuts import render

# Create your views here.
def product_reviews(request):
    """ A view to show reviews for the product """

    product_reviews = ProductReview.objects.all()
    template = 'reviews/includes/reviews.html'
    context = {
        'product_reviews': product_reviews,
    }

    return render(request, template, context)
