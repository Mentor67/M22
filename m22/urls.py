from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

  path('', views.HomeView.as_view(), name='home'),


  path('machines/', views.MachineView.as_view(), name="machines"),
  path('providers/', views.ProviderView.as_view(), name='providers'),
  path("parts/", views.PartView.as_view(), name="parts"),
  path("maintenances/", views.MaintenanceView.as_view(), name="maintenances"),
  path("materials/", views.MaterialView.as_view(), name="materials"),
  path("labors/", views.LaborView.as_view(), name="labors"),
  path("<pk>/machines/", views.MachineDetailView.as_view(), name="machine_1"),


  path('machines/new/', views.MachineCreateView.as_view(), name='new_machine'),
  path('providers/new/', views.ProviderCreateView.as_view(), name='new_provider'),
  path('parts/new/', views.PartCreateView.as_view(), name='new_part'),
  path('maintenances/new/', views.MaintenanceCreateView.as_view(), name='new_maintenance')
              ]

urlpatterns += staticfiles_urlpatterns()