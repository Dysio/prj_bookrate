from django import forms
from .models import Rate

RATINGS = [('1',1),('2',2),('3',3),('4',4),('5',5)]

class RateForm(forms.ModelForm):
    rate = forms.IntegerField(
        label='rate',
        widget=forms.Select(choices=RATINGS),
    )


    class Meta:
        model = Rate
        fields = ('rate',)