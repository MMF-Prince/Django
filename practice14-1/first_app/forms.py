from django import forms
from django.forms.widgets import NumberInput  #its for calender
import datetime
from .models import MyModel
# #char_field
# class ExampleForm(forms.Form):
#     name = forms.CharField(max_length=10,initial='your name')

# #char_TextArea
# class ExampleForm(forms.Form):
#     comment=forms.CharField(widget=forms.Textarea)

# #char_textarea_eith_widget_attribute
# class ExampleForm(forms.Form):
#     comment2=forms.CharField(widget=forms.Textarea(attrs={'row': 3}))

# #email
# class ExampleForm(forms.Form):
#     email=forms.EmailField(label='Please write your email here')

# #boolean_field
# class ExampleForm(forms.Form):
#     agree=forms.BooleanField()

# #date_field
# class ExampleForm(forms.Form):
#     date=forms.DateField(initial=datetime.date.today)

# #calender_Field
# class ExampleForm(forms.Form):
#     birth_date= forms.DateField(widget=NumberInput(attrs={'type':'date'}))

# #date Field from selected data
# Birth_Years=['2000','2004','2008']
# class ExampleForm(forms.Form):
#     birth_year=forms.DateField(widget=forms.SelectDateWidget(years=Birth_Years))

# #Decimal_Field
# class ExampleForm(forms.Form):
#     value=forms.DecimalField(required=False)

#Coice_Field
# Fav_Col=[
#     ('blue','Blue'),
#     ('green','Green'),
#     ('red','Red')
# ]
# class ExampleForm(forms.Form):
#     fav_col=forms.ChoiceField(choices=Fav_Col)

# class ExampleForm(forms.Form):
#     fav_col2=forms.ChoiceField(widget=forms.RadioSelect,choices=Fav_Col)
    
# class ExampleForm(forms.Form):
#     fav_col3=forms.MultipleChoiceField(choices=Fav_Col)

# class ExampleForm(forms.Form):
#     fav_col4=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Fav_Col)



#Below this line is for model form



class ExampleForm(forms.ModelForm):
    class Meta:
        model=MyModel
        fields='__all__'