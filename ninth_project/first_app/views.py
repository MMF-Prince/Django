from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse

# Create your views here.

def home(request):
    response=render(request,'home.html')
    response.set_cookie('name','rahim')
    # response.set_cookie('name','karim',max_age=10)
    response.set_cookie('name','karim',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name=request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response=render(request,'del.html')
    response.delete_cookie('name')
    return response

#Django Session
#Session vs cookies

def set_session(request):
    data={
        'name':'rahim',
        'age':23,
        'language':'Bangla'
    }
    request.session.update(data)
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:
        name=request.session.get('name','Guest')
        request.session.modified=True
        return render(request,'get_session.html',{'name':name})
    else:
        return HttpResponse("Your session has been expired.")

def delete_session(request):
    del request.session['name']
    return render(request,'del.html')