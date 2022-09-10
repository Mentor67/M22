from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Machine, Provider, Part, Maintenance, Material, Labor 

# Create your views here.
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