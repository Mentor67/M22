# Generated by Django 3.2.15 on 2022-10-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m22', '0003_remove_maintenance_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='link',
            field=models.CharField(default='https://www.emag.ro', max_length=500),
        ),
    ]
