from django import forms
from .models import Sale
class SaleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            'first_name',
            'last_name',        
            'age',
            'person',
        )