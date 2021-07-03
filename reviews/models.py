from django.db import models

from profiles.models import Profile
from products.models import Product

# Create your models here.

class ProductReview(models.Model):

    RATING_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
    )

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    headline = models.CharField(max_length=50, null=False, blank=False)
    comments = models.CharField(max_length=1200, null=False, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
