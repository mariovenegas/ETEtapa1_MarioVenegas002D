from django import forms
from django.forms import ModelForm
from .models import Proveedor
from .models import Insumo

class ProveedorForm(ModelForm):
    class Meta:
        model= Proveedor
        fields =['numeroIdentificacion', 'nombre','telefono','direccion','email','pais','moneda']

class InsumoForm(ModelForm):
    class Meta:
        model= Insumo
        fields =['idInsumo','nombre','descripcion','proveedor']