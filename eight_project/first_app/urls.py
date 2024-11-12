from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.signup,name='signup'),
    path('', views.home,name='homepage'),
    path('login/', views.userlogin,name='login'),
    path('profile/', views.profile,name='profile'),
    path('logout/', views.user_logout,name='logout'),
    path('pass_change/', views.pass_change,name='passchange'),
    path('change_user_data/', views.change_user_data,name='datachange'),
]