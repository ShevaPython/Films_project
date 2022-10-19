from django import forms


from .models import Reviews,Movie


class ReviewsForm(forms.ModelForm):
    '''Форма отзыва'''
    class Meta:
        model=Reviews
        fields=['name','email','text']



