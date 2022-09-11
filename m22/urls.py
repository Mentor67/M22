from django.urls import path, include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

  path('', views.HomeView.as_view(), name='home'),
  path('machines/', views.MachineView.as_view(), name="machines"),
  
              ]