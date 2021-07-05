from django.contrib import admin
from .models import Proveedor, Pais, Insumo

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Pais)
admin.site.register(Insumo)
