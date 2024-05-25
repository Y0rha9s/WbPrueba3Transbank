from django.shortcuts import render
from compra_ahorra.views import Carrito
from compra_ahorra.models.models import Producto

def tienda(request):
    productos = Producto.objects.all()
    return render(request,"index.html",{'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return render(request,'index.html')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return render(request,'index.html')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return render(request,'index.html')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request,'index.html')