# Generated by Django 3.2.23 on 2024-01-30 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0, verbose_name='Cantidad'),
        ),
    ]
