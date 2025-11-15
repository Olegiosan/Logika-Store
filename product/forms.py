from django import forms

from product.models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "cost", "count"]
