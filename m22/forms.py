from django import forms
from django.core.exceptions import ValidationError
from .models import Machine



class MachineForm(forms.ModelForm):
    class Meta:

        model = Machine
        fields = ('name',
                  'description',
                  'serial_number',
                  'manufactured',
                  'commissioned',
                  'price',
                  'machine_category',
                  'machine_status',
                  'user',
                  )

    def clean_name(self):
        name = self.cleaned_data['name']
        if "django" not in name:
            raise ValidationError("Please add _")
        return name


        # name = models.CharField(max_length=200)
        # description = models.CharField(max_length=200)
        # serial_number = models.CharField(max_length=14)
        # manufactured = models.DateField()
        # commissioned = models.DateField()
        # price = models.FloatField(default=0)
        # machine_category = models.ForeignKey(MachineCategory, on_delete=models.CASCADE)
        # machine_status = models.ForeignKey(MachineStatus, on_delete=models.CASCADE)
        # created_on = models.DateField(auto_now_add=True)
        # modified_on = models.DateField(auto_now=True)
        # user = models.ForeignKey(User, on_delete=models.CASCADE)