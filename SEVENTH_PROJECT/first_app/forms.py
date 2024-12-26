from django import forms
from first_app.models import StudentMOdel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentMOdel
        fields='__all__'
        labels={
            'name':'Student Name',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'btn-danger'}),

        }
        help_texts={
            'name':"Write your full name"
        }
        error_messages={
            'name': {'required':'your name is required'}
        }