
from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index),
    path('new', views.new),
    path('firstpg', views.firstpg, name='firstpg'),
    path('fbpage', views.fbpage, name='fbpage'),
    path('calculator', views.calculator, name='calculator'),
]
