# Generated by Django 4.2.3 on 2023-08-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0005_empleado_hojavida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres_completo'),
        ),
    ]
