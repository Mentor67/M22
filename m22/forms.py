from django import forms
from django.core.exceptions import ValidationError
from .models import Machine
from .models import Provider
from .models import Part
from .models import Maintenance
from .models import Material
from .models import Labor


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = (
            'name',
            'description',
            'serial_number',
            'manufactured',
            'commissioned',
            'price',
            'machine_category',
            'machine_status',
            'user',
        )

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control my-1 col-md-4',
                'placeholder': "enter the machine name"

            }),
        }

        labels = {
            'name': "Machine name"
        }

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if "django" not in name:
    #         raise ValidationError("Please add _")
    #     return name


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = (
            'name',
            'provider_type',
            'provider_status',
            'user',
        )


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = (
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
        )


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = (
            'machine',
            'maintenance_date',
            'maintenance_status',
            'user',
            'maintenance_type',
        )


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            'maintenance',
            'part',
            'qty',
            'user',
        )


class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = (
            'maintenance',
            'provider',
            'document',
            'value',
            'user',
        )
