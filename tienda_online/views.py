from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos, Categorias
from .forms import UserRegisterForm, FormProducto
from django.contrib import messages
from django.contrib.auth.decorators import permission_required


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


@permission_required('tienda_online.add_productos')
def producto_nuevo(request):
    if request.method == 'POST':
        form = FormProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_nuevo')
    else:
        form = FormProducto()
    context = {'form': form}
    return render(request, 'tienda_online/producto_nuevo.html', context)


@permission_required('tienda_online.change_productos')
def producto_editar(request, id):
    producto = get_object_or_404(Productos, id=id)
    data = {
        'form': FormProducto(instance=producto)
    }
    if request.method == 'POST':
        form = FormProducto(data=request.POST,
                            instance=producto, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_nuevo')
        data["form"] = form
    else:
        form = FormProducto()
    context = {'form': form}
    return render(request, 'tienda_online/producto_editar.html', data)


@permission_required('tienda_online.delete_productos')
def producto_eliminar(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    return redirect('index')
