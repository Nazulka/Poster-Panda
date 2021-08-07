from django import forms
from .models import ProductReview


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ('user', 'product', 'date_posted')
        fields = ['headline', 'comments', 'rating']
        labels = {
            'rating': 'Select Your Rating',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'headline': 'Review Headline',
            'comments': 'Your Comments',
        }

        self.fields['headline'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field != 'rating':
                placeholder = f'{placeholders[field]} *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
