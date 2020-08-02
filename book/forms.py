from django import forms
from .models import Rate

class RateForm(forms.ModelForm):
    rate = forms.IntegerField(
        label='rate'
    )

    class Meta:
        model = Rate
        fields = ('rate',)