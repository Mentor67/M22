from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  # """home url"""
  path('', views.HomeView.as_view(), name='home'),

  # """list urls"""
  path('machines/', views.MachineView.as_view(), name="machines"),
  path('active_machines/', views.ActiveMachinesView.as_view(), name="active_machines"),
  path('in_service_machines/', views.InServiceMachinesView.as_view(), name="in_service_machines"),

  path('providers/', views.ProviderView.as_view(), name='providers'),
  path('active_providers/', views.ActiveProviderView.as_view(), name='active_providers'),
  path('inactive_providers/', views.InactiveProviderView.as_view(), name='inactive_providers'),

  path("parts/", views.PartView.as_view(), name="parts"),
  path("maintenances/", views.MaintenanceView.as_view(), name="maintenances"),
  path("materials/", views.MaterialView.as_view(), name="materials"),
  path("labors/", views.LaborView.as_view(), name="labors"),

  # """detail urls"""
  path("<pk>/machines/", views.MachineDetailView.as_view(), name="machine_detail"),
  path("<pk>/providers/", views.ProviderDetailView.as_view(), name="provider_detail"),
  path("<pk>/parts/", views.PartDetailView.as_view(), name="part_detail"),
  path("<pk>/maintenances/", views.MaintenanceDetailView.as_view(), name="maintenance_detail"),
  path('<pk>/materials/', views.MaterialDetailView.as_view(), name="material_detail"),
  path('<pk>/labors/', views.LaborDetailView.as_view(), name="labor_detail"),

  # """create urls"""
  path('machines/new/', views.MachineCreateView.as_view(), name='new_machine'),
  path('providers/new/', views.ProviderCreateView.as_view(), name='new_provider'),
  path('parts/new/', views.PartCreateView.as_view(), name='new_part'),
  path('maintenances/new/', views.MaintenanceCreateView.as_view(), name='new_maintenance'),
  path('materials/new/', views.MaterialCreateView.as_view(), name="new_material"),
  path('labors/new/', views.LaborCreateView.as_view(), name="new_labor"),

  # """delete urls"""
  path("<pk>/machines/delete/", views.MachineDeleteView.as_view(), name="delete_machine"),
  path("<pk>/providers/delete/", views.ProviderDeleteView.as_view(), name="delete_provider"),
  path('<pk>/parts/delete/', views.PartDeleteView.as_view(), name="delete_part"),
  path("<pk>/maintenances/delete", views.MaintenanceDeleteView.as_view(), name="delete_maintenance"),
  path("<pk>/materials/delete", views.MaterialDeleteView.as_view(), name="delete_material"),
  path('<pk>/labor/delete', views.LaborDeleteView.as_view(), name="delete_labor"),

  # """create urls"""
  path("<pk>/machines/edit/", views.MachineUpdateView.as_view(), name="edit_machine"),

              ]

urlpatterns += staticfiles_urlpatterns()