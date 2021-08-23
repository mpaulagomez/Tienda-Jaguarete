from .carro import Carro

def importe_total(request):
    carro=Carro(request)
    total=0
    for key, value in request.session["carro"].items():
        total=total+(float(value["precio"]))
    return {"importe_total":total}
