from django.shortcuts import render
from .models import Productos


def index(request):
    productos = Productos.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda_online/index.html', context)


def acerca_de(request):
    return render(request, 'tienda_online/acerca_de.html')
