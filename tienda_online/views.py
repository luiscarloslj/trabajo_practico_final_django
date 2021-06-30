from django.shortcuts import render, redirect
from .models import Productos
from .forms import UserRegisterForm
from django.contrib import messages


def index(request):
    productos = Productos.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda_online/index.html', context)


def acerca_de(request):
    return render(request, 'tienda_online/acerca_de.html')


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('index')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'tienda_online/registro.html', context)


def producto_detalles(request, pk):
    productos = Productos.objects.get(id=pk)
    context = {'productos': productos}
    return render(request, 'tienda_online/producto_detalles.html', context)
