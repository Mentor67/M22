from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  # """home url"""
  path('', views.HomeView.as_view(), name='home'),

  # """list urls"""
  path('machines/', views.MachineView.as_view(), name="machines"),
  path('active_machines/', views.ActiveMachinesview.as_view(), name="active_machines"),
  path('providers/', views.ProviderView.as_view(), name='providers'),
  path("parts/", views.PartView.as_view(), name="parts"),
  path("maintenances/", views.MaintenanceView.as_view(), name="maintenances"),
  path("materials/", views.MaterialView.as_view(), name="materials"),
  path("labors/", views.LaborView.as_view(), name="labors"),

  # """detail urls"""
  path("<pk>/machines/", views.MachineDetailView.as_view(), name="machine_detail"),
  path("<pk>/providers/", views.ProviderDetailView.as_view(), name="provider_detail"),
  path("<pk>/parts/", views.PartDetailView.as_view(), name="part_detail"),
  path("<pk>/maintenances/", views.MaintenanceDetailView.as_view(), name="maintenance_detail"),

  # """create urls"""
  path('machines/new/', views.MachineCreateView.as_view(), name='new_machine'),
  path('providers/new/', views.ProviderCreateView.as_view(), name='new_provider'),
  path('parts/new/', views.PartCreateView.as_view(), name='new_part'),
  path('maintenances/new/', views.MaintenanceCreateView.as_view(), name='new_maintenance'),
  path('materials/new/', views.MaterialCreateView.as_view(), name="new_material"),
  path('labors/new/', views.LaborCreateView.as_view(), name="new_labor"),

  # """delete urls"""

  path("<pk>/machines/delete/", views.MachineDeleteView.as_view(), name="delete_machine"),
              ]

urlpatterns += staticfiles_urlpatterns()