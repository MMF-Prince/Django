from django import forms 
from django.core import validators

#widgets ==field to html input
class contactForm(forms.Form):
    name=forms.CharField(label="User Name",initial='Rahim',help_text='Total length withn 10 char', widget=forms.Textarea(attrs={'id':'text_area','placeholder':'Enter Your Name'}))
    # file=forms.FileField()
    # email=forms.EmailField(label="user E-mail")
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    birthday=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appoinment=forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    CHOICES=[('S','Small'),('L','Large'),('M','Medium')]
    size=forms.ChoiceField( choices=CHOICES,widget=forms.RadioSelect)
    meal=[('P','Pepparoni'),('M','Mashroom')]
    pizza=forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name=forms.CharField()
#     email=forms.EmailField()
#     # def clean_name(self):
#     #     valname=self.cleaned_data['name']
#     #     if len(valname) <10:
#     #         raise forms.ValidationError("Enter a Name with atleast 10 char")
#     #     return valname
#     # def clean_email(self):
#     #     valemail=self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Please enter a valid email address")
#     #     return valemail

#     def clean(self):
#         cleaned_data =super().clean()
#         valname=self.cleaned_data['name']
#         valemail=self.cleaned_data['email']
#         if len(valname) <10:
#             raise forms.ValidationError("Enter a Name with atleast 10 char")
    
#         if '.com' not in valemail:
#             raise forms.ValidationError("Please enter a valid email address")


class StudentData(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(10,message="Atleast 10 char")])
    email=forms.EmailField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid Email")])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34,message='age must be below 34'),validators.MinValueValidator(20,message="Age must be above 20")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'])])
    #django validators: regex, url

class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        val_pass=self.cleaned_data['password']
        val_compass=self.cleaned_data['confirm_password']
        val_name=self.cleaned_data['name']
        if val_pass != val_compass:
            raise forms.ValidationError("password dosen't match")
        if len(val_name)<10:
            raise forms.ValidationError("Name must be 15 character")
