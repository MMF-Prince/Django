from django.shortcuts import render
from album.models import Album,Musician
# from musician.models import musician
# from album.models import album

def home(request):
    data=Album.objects.all()
    data2=Musician.objects.all()
    return render(request,'home.html',{'data':data,'data2':data2})