from django import forms
from . import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.AutoParts
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.ReviewProducts
        fields = "__all__"