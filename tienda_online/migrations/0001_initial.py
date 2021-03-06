# Generated by Django 3.2.4 on 2021-06-24 00:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('contenido', models.CharField(max_length=1000)),
                ('precio', models.IntegerField()),
                ('image', models.ImageField(default='vacio.png', upload_to='')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
