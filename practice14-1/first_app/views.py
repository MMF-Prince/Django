from django.shortcuts import render,redirect
from .forms import ExampleForm
# Create your views here.

def Example(request):
    form=ExampleForm(request.POST)
    return render(request,'forms.html',{'form':form})
