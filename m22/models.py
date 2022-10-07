
from django.db import models
from django.contrib.auth.models import User


class MachineCategory(models.Model):
    category = models.CharField(max_length=30)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return "/machines"

    def __str__(self):
        return f"""
        {self.category}
        """


class MachineStatus(models.Model):
    status = models.CharField(max_length=30)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return "/machines"

    def __str__(self):
        return f"""
        {self.status}
        """


class Machine(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=14)
    manufactured = models.DateField()
    commissioned = models.DateField()
    price = models.FloatField(default=0)
    machine_category = models.ForeignKey(MachineCategory, on_delete=models.CASCADE)
    machine_status = models.ForeignKey(MachineStatus, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "/machines"

    def __str__(self):
        return f"""
        name: {self.name}
        description: {self.description}
        price: {self.price}
        status: {self.machine_status}
        """


class ProviderType(models.Model):
    type = models.CharField(max_length=10)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return "/providers"

    def __str__(self):
        return f"""
        {self.type}
        """


class ProviderStatus(models.Model):
    status = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return "/providers"

    def __str__(self):
        return f"""
        {self.status}
        """


class Provider(models.Model):
    name = models.CharField(max_length=200)
    provider_type = models.ForeignKey(ProviderType, on_delete=models.CASCADE)
    provider_status = models.ForeignKey(ProviderStatus, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "/providers"

    def __str__(self):
        return f"""
        name: {self.name}
        status: {self.provider_status}
        """


class PartCategory(models.Model):
    category = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return "/parts"

    def __str__(self):
        return f"""
        {self.category}
        """


class Part(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    part_category = models.ForeignKey(PartCategory, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    stock = models.FloatField(default=0)
    mu = models.CharField(max_length=2)
    target_stock = models.FloatField(default=0)
    provider_status = models.ForeignKey(ProviderStatus, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=500, default="https://www.emag.ro/")

    @property
    def diff_stock(self):
        return self.target_stock - self.stock

    @property
    def val_diff_stock(self):
        return (self.target_stock - self.stock) * self.price



    def get_absolute_url(self):
        return "/parts"

    def __str__(self):
        return f"""
        name: {self.name};
        price: {self.price};
        category: {self.part_category};
        stock: {self.stock};
        unit: {self.mu};
        target_stock: {self.target_stock};
        status: {self.provider_status};
        """


class MaintenanceType(models.Model):
    type = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return "/maintenances"

    def __str__(self):
        return f"""
         {self.type}
        """


class MaintenanceStatus(models.Model):
    status = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "/maintenances"

    def __str__(self):
        return f"""
         {self.status}
        """


#   def save(self, *args, **kwargs):
#       user = get_current_user()
#       self.user = user
#       super(MaintenanceStatus, self).save(*args, **kwargs)

class Maintenance(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    maintenance_status = models.ForeignKey(MaintenanceStatus, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "/maintenance"

    def __str__(self):
        return f"""
         {self.id}
         {self.machine.name}
         {self.maintenance_status}
         {self.maintenance_type}
        """


class Material(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    qty = models.FloatField(default=0)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "/materials"

    def __str__(self):
        return f"""
        {self.maintenance.id}
        name: {self.part.name}
        qty: {self.qty};

        """


class Labor(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    document = models.CharField(max_length=5)
    value = models.FloatField(default=0)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return "/labor"

    def __str__(self):
        return f"""
        document: {self.document}
        value: {self.value};

        """
