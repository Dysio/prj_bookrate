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

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user')
    #     super(RateForm, self).__init__(*args, **kwargs)


    class Meta:
        model = RateTest
        fields = ['rate', 'book', 'user']
        # fields = ['rate',]