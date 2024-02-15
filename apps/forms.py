from django import forms
from apps.models import ProductModel


class CarbonadForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
