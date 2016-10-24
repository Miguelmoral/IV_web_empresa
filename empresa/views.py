from django.shortcuts import render


from .models import Datos
from .forms import MyForm


def principal(request):

    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            clasificacion = Datos.objects.order_by('-puntuacion')
            context = {'clasificacion': clasificacion}
            return render(request, 'empresa/clasificacion.html', context)

    else:
        form = MyForm()
    return render(request, 'empresa/principal.html', {'form':form})


def clasificacion(request):
    clasificacion = Datos.objects.order_by('-puntuacion')
    context = {'clasificacion': clasificacion}
    return render(request, 'empresa/clasificacion.html', context)

def delete(request):

        if request.method == "POST":
            form = MyForm(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data['nombre_empresa']
                emp = Datos.objects.get(nombre_empresa = nombre)
                emp.delete()
                return render(request, 'empresa/principal.html', {'form':form})

        else:
            form = MyForm()
        return render(request, 'empresa/delete.html', {'form':form})
