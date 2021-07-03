from django import forms
from .models import ProductReview


class AddReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        exclude = ('user', 'product', 'date_posted')
        fields = ('headline', 'comments', 'rating')
        labels = {
            'rating': 'Rating',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Add placeholders for form input fields
        """

        placeholders = {
            'headline': 'I would buy this product again',
            'comments': 'Things are great about this product and things not so great about it.',
            
        }
        self.fields['headline'].widget.attrs['autofocus'] = True
        self.fields['comments'].widget.attrs['rows'] = 5
        
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].label = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'