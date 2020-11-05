from django.urls import path
from .views import Home,About,Plant,Pot,Ball

urlpatterns = [
    path('', Home,name='home-page'),
    path('home/', Home,name='home-page'),
    path('about/',About,name='about-page'),
    path('plant/',Plant,name='plant-page'),
    path('pot/',Pot,name='pot-page'),
    path('ball/',Ball,name='')

]