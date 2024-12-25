from django import forms
from .models import Catagory

class CatagoryForm(forms.ModelForm):
    class Meta:
        model= Catagory
        fields='__all__'
        # fields=['name','bio']
        # exclude=['name','bio']