from django.urls import path
from . import views
urlpatterns = [
    path('',views.set_session),
    path('get/',views.get_cookie),
    path('del/',views.delete_session),
    path('gets/',views.get_session),
]
