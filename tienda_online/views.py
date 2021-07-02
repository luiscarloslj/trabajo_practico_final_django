from django.shortcuts import render, redirect
from .models import Productos, Categorias
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
    producto = Productos.objects.get(id=pk)
    context = {'producto': producto}
    return render(request, 'tienda_online/producto_detalles.html', context)


def busqueda(request):
    categoriaID = request.GET.get('categoria')
    # if pk:
    #     categoria = Categorias.objects.get(id=pk)
    #     context = {'categoria': categoria}
    #     return render(request, 'tienda_online/busqueda.html', context)
    if categoriaID == None:
        if request.method == 'POST':
            buscando = request.POST.get('buscando')
            productos_e = Productos.objects.filter(titulo__contains=buscando)
            return render(request, 'tienda_online/busqueda.html', {'buscando': buscando, 'productos_e': productos_e})
        else:
            return render(request, 'tienda_online/busqueda.html')
    else:
        productos = Productos.objects.filter(categoria_id=categoriaID)

        context = {'productos': productos}
        return render(request, 'tienda_online/busqueda.html', context)
