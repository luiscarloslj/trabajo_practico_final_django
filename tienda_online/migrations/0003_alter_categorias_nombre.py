# Generated by Django 3.2.4 on 2021-07-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_online', '0002_auto_20210624_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]
