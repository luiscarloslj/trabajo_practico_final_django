from tienda_online.models import Categorias


def categorias_a(request):
    categorias = Categorias.objects.all()
    return {'categorias': categorias}


def importe_total_carro(request):
    total = 0
    # if request.user.is_authenticated:
    for key, value in request.session["carro"].items():
        total = total+int(value["precio"])

    return {"importe_total_carro": total}
