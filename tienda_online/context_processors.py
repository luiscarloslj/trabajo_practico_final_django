from tienda_online.models import Categorias


def categorias_a(request):
    categorias = Categorias.objects.all()
    return {'categorias': categorias}
