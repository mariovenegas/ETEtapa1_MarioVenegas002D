from django.shortcuts import render, redirect
from .models import Proveedor
from .models import Insumo
from .forms import ProveedorForm
from .forms import InsumoForm

# Create your views here.
def inicio(request):
    return render(request,'groundZero/inicio.html')

def proveedor(request):
    proveedores = Proveedor.objects.all()
    datos = {
        'proveedores': proveedores
    }
    return render(request,'groundZero/proveedor.html',datos)

def insumo(request):
    insumos = Insumo.objects.all()
    datos = {
        'insumos': insumos
    }
    return render(request,'groundZero/insumo.html',datos)

def form_proveedor(request):
    datos={
        'form':ProveedorForm()
    }
    if request.method =='POST':
        formulario=ProveedorForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos guardados correctamente"
    return render(request,'groundZero/form_proveedor.html',datos)


def form_insumo(request):
    datos={
        'form':InsumoForm()
    }
    if request.method =='POST':
        formulario=InsumoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos guardados correctamente"
    return render(request,'groundZero/form_insumo.html',datos)

def form_mod_proveedor(request,id):
    proveedor = Proveedor.objects.get(numeroIdentificacion=id)

    datos = {
        'form':ProveedorForm(instance=proveedor)
    }
    if request.method =='POST':
        formulario=ProveedorForm(data=request.POST,instance=proveedor)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos modificados correctamente"    
    return render(request,'groundZero/form_mod_proveedor.html',datos)

def form_mod_insumo(request,id):
    insumo = Insumo.objects.get(idInsumo=id)

    datos = {
        'form':InsumoForm(instance=insumo)
    }
    if request.method =='POST':
        formulario=InsumoForm(data=request.POST,instance=insumo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos modificados correctamente"
    return render(request,'groundZero/form_mod_insumo.html',datos)

def form_del_proveedor(request,id):
    proveedor=Proveedor.objects.get(numeroIdentificacion=id)
    proveedor.delete()
    return redirect(to="proveedor")

def form_del_insumo(request,id):
    insumo=Insumo.objects.get(idInsumo=id)
    insumo.delete()
    return redirect(to="insumo")    