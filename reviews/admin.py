from django.contrib import admin
from .models import ProductReview

# Register your models here.

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'headline',
        'comments',
        'rating',
        'date_posted'
    )


admin.site.register(ProductReview, ProductReviewAdmin)
