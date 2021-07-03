from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_reviews, name="product_reviews"),
    path('add_review/', views.add_review, name='add_review'),
]