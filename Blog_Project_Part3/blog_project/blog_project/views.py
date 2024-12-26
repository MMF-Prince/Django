from django.shortcuts import render
from post.models import Post
from catagories.models import Catagory

def home(request,catagory_slug=None):
    data=Post.objects.all()
    if catagory_slug is not None:
        catagory=Catagory.objects.get(slug=catagory_slug)
        data=Post.objects.filter(catagory=catagory)
    catagories=Catagory.objects.all()
    return render(request,'home.html',{'data' : data,'catagories' : catagories})