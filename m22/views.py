from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic import ListView

from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Machine
from .models import Provider
from .models import Part
from .models import Maintenance
from .models import Material
from .models import Labor

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
        context['my_name'] = 'Andrei'
        return context


class MachineView(TemplateView):
    template_name = "m22/machine.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["machines"] = Machine.objects.all()
        context["active_machines"] = Machine.objects.filter(machine_status=1)
        context["in_service_machines"] = Machine.objects.filter(machine_status=2)
        context['name'] = 'Machines List'
        return context


class ProviderView(TemplateView):
    template_name = "m22/provider.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["providers"] = Provider.objects.all()
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


class MachineDetailView(generic.DetailView):
    context_object_name = 'machine_detail'
    model = Machine
    template_name = "m22/machine_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super(MachineDetailView, self).get_context_data(**kwargs)
    #     ## the context is a list of the tasks of the Project##
    #     ##THIS IS THE ERROR##
    #     context['maintenance'] = Maintenance.objects.all()


# Form views

class MachineCreateView(CreateView):
    template_name = "m22/new_machine.html"

    model = Machine
    fields = [
        'name',
        'description',
        'serial_number',
        'manufactured',
        'commissioned',
        'price',
        'machine_category',
        'machine_status',
        'user',
    ]
    success_url = '/machines/'


class ProviderCreateView(CreateView):
    template_name = "m22/new_provider.html"

    model = Provider
    fields = [
        'name',
        'provider_type',
        'provider_status',
        'user',
    ]
    success_url = '/providers/'


class PartCreateView(CreateView):
    template_name = "m22/new_part.html"
    model = Part
    fields = [
        'name',
        'description',
        'price',
        'part_category',
        'provider',
        'stock',
        'mu',
        'target_stock',
        'provider_status',
        'user',
    ]
    success_url = '/parts/'


class MaintenanceCreateView(CreateView):
    template_name = "m22/new_maintenance.html"
    model = Maintenance
    fields = [
        'machine',
        'maintenance_date',
        'maintenance_status',
        'user',
        'part',
        'maintenance_type',
    ]
    success_url = '/maintenances/'
