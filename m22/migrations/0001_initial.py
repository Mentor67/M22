# Generated by Django 3.2.13 on 2022-09-06 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=14)),
                ('manufactured', models.DateField()),
                ('commissioned', models.DateField()),
                ('price', models.FloatField(default=0)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MachineCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MachineStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_date', models.DateField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.machine')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('provider_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.providerstatus')),
                ('provider_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.providertype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField(default=0)),
                ('stock', models.FloatField(default=0)),
                ('mu', models.CharField(max_length=2)),
                ('target_stock', models.FloatField(default=0)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('part_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.partcategory')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.provider')),
                ('provider_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.providerstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField(default=0)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.maintenance')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.part')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='maintenance',
            name='maintenance_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.maintenancestatus'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='maintenance_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.maintenancetype'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.part'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='machine',
            name='machine_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.machinecategory'),
        ),
        migrations.AddField(
            model_name='machine',
            name='machine_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.machinestatus'),
        ),
        migrations.AddField(
            model_name='machine',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(max_length=5)),
                ('value', models.FloatField(default=0)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.maintenance')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='m22.provider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
