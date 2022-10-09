from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic import ListView

from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from .models import Machine
from .models import Provider
from .models import Part
from .models import Maintenance
from .models import Material
from .models import Labor
from .models import MachineStatus
from .models import ProviderStatus

from .forms import MachineForm
from .forms import ProviderForm
from .forms import PartForm
from .forms import MaintenanceForm
from .forms import MaterialForm
from .forms import LaborForm

from django.views import generic


class HomeView(TemplateView):
    template_name = "m22/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["machines"] = Machine.objects.all()
        context["providers"] = Provider.objects.all()
        context["parts"] = Part.objects.all()
        context["maintenances"] = Maintenance.objects.all()
        context["materials"] = Material.objects.all()
        context["labors"] = Labor.objects.all()
        return context


class MachineView(TemplateView):
    template_name = "m22/machine.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["machines"] = Machine.objects.all()
        context['name'] = 'Machines List'
        return context


class ActiveMachinesView(TemplateView):
    template_name = "m22/active_machine.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_status = MachineStatus.objects.get(status="active")
        context["active_machines"] = Machine.objects.filter(machine_status=active_status)
        context['name'] = 'Active Machines List'
        return context


class InServiceMachinesView(TemplateView):
    template_name = "m22/in_service_machine.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        in_service_status = MachineStatus.objects.get(status='in service')
        context["in_service_machines"] = Machine.objects.filter(machine_status=in_service_status)
        context['name'] = 'In Service Machines List'
        return context


class ProviderView(TemplateView):
    template_name = "m22/provider.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["providers"] = Provider.objects.all()
        return context


class ActiveProviderView(TemplateView):
    template_name = "m22/active_provider.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_status = ProviderStatus.objects.get(status="active")
        context["active_providers"] = Provider.objects.filter(provider_status=active_status)
        return context


class InactiveProviderView(TemplateView):
    template_name = "m22/inactive_provider.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inactive_status = ProviderStatus.objects.get(status="inactive")
        context["inactive_providers"] = Provider.objects.filter(provider_status=inactive_status)
        return context


class PartView(TemplateView):
    template_name = "m22/part.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["parts"] = Part.objects.all()
        return context


class MaintenanceView(TemplateView):
    template_name = "m22/maintenance.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["maintenances"] = Maintenance.objects.all()
        return context


class MaterialView(TemplateView):
    template_name = "m22/material.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materials'] = Material.objects.all()
        return context


class LaborView(TemplateView):
    template_name = "m22/labor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['labors'] = Labor.objects.all()
        return context


# Detail Views
class MachineDetailView(generic.DetailView):
    context_object_name = 'machine_detail'
    model = Machine
    template_name = "m22/machine_detail.html"


class ProviderDetailView(generic.DetailView):
    context_object_name = 'provider_detail'
    model = Provider
    template_name = "m22/provider_detail.html"


class PartDetailView(generic.DetailView):
    context_object_name = 'part_detail'
    model = Part
    template_name = "m22/part_detail.html"


class MaintenanceDetailView(generic.DetailView):
    context_object_name = 'maintenance_detail'
    model = Maintenance
    template_name = "m22/maintenance_detail.html"


class MaterialDetailView(generic.DetailView):
    context_object_name = 'material_detail'
    model = Material
    template_name = "m22/material_detail.html"


class LaborDetailView(generic.DetailView):
    context_object_name = 'labor_detail'
    model = Labor
    template_name = "m22/labor_detail.html"


# Form views

class MachineCreateView(CreateView):
    template_name = "m22/new_machine.html"

    model = Machine
    success_url = '/machines/'
    form_class = MachineForm


class ProviderCreateView(CreateView):
    template_name = "m22/new_provider.html"

    model = Provider
    success_url = '/providers/'
    form_class = ProviderForm


class PartCreateView(CreateView):
    template_name = "m22/new_part.html"

    model = Part
    success_url = '/parts/'
    form_class = PartForm


class MaintenanceCreateView(CreateView):
    template_name = "m22/new_maintenance.html"

    model = Maintenance
    success_url = '/maintenances/'
    form_class = MaintenanceForm


class MaterialCreateView(CreateView):
    template_name = "m22/new_material.html"

    model = Material
    success_url = '/materials/'
    form_class = MaterialForm


class LaborCreateView(CreateView):
    template_name = 'm22/new_labor.html'

    model = Labor
    success_url = '/labors/'
    form_class = LaborForm


# Delete views


class MachineDeleteView(DeleteView):
    template_name = 'm22/delete_machine.html'
    model = Machine
    success_url = '/machines/'


class ProviderDeleteView(DeleteView):
    template_name = 'm22/delete_provider.html'
    model = Provider
    success_url = '/providers/'


class PartDeleteView(DeleteView):
    template_name = 'm22/delete_part.html'
    model = Part
    success_url = '/parts/'


class MaintenanceDeleteView(DeleteView):
    template_name = 'm22/delete_maintenance.html'
    model = Maintenance
    success_url = '/maintenances/'


class MaterialDeleteView(DeleteView):
    template_name = 'm22/delete_material.html'
    model = Material
    success_url = '/materials/'


class LaborDeleteView(DeleteView):
    template_name = 'm22/delete_labor.html'
    model = Labor
    success_url = '/labors/'


# Update Views

class MachineUpdateView(UpdateView):
    template_name = "m22/new_machine.html"

    model = Machine
    success_url = '/machines/'
    form_class = MachineForm
