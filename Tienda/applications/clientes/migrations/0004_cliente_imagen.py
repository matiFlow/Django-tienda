# Generated by Django 3.2 on 2024-03-10 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(null=True, upload_to='clientes'),
        ),
    ]
