
from django.urls import path
from . import views

urlpatterns = [
   path('reg', views.reg),
   path('login', views.logintodo, name='logintodo'),
   path('hometodo', views.hometodo, name='hometodo'),
   path('craccount', views.craccount, name='craccount')
   ]
 