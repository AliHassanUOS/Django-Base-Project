from collections import namedtuple
from django.urls import path
from .views import home
from .views import home
from student import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [


    path("", views.home,name='home'),
    path("del/", views.fun,name="del"),
    path('update/<myid>', views.update,name = "update")

 
]