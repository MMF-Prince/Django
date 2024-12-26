from django.urls import path,include
from . import views
urlpatterns = [
    path('forms/', views.Example,name='aboutPage'),
]