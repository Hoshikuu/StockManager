from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'inventario/lista.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tallas = [request.POST.get('35'), request.POST.get('36'), request.POST.get('37'), request.POST.get('38'), request.POST.get('39'), request.POST.get('40'), request.POST.get('41'), request.POST.get('42'), request.POST.get('43'), request.POST.get('44'), request.POST.get('45'), request.POST.get('46'),]
        if nombre and tallas:
            Producto.objects.create(nombre=nombre, tallas=tallas)
            return redirect('lista')
    return render(request, 'inventario/agregar.html')