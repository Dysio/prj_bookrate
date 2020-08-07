from django import forms
from .models import RateTest

RATINGS = [('1',1),('2',2),('3',3),('4',4),('5',5)]

class RateForm(forms.ModelForm):
    rate = forms.IntegerField(
        label='rate',
        widget=forms.Select(choices=RATINGS),
    )
    book = forms.CharField(label='book id')
    user = forms.CharField(label='user id')

    class Meta:
        model = RateTest
        fields = ['rate', 'book', 'user']
        # fields = ['rate',]