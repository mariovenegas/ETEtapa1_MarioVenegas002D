from django.urls import path
from .views import inicio
from .views import proveedor
from .views import insumo,form_insumo, form_proveedor, form_mod_insumo, form_mod_proveedor, form_del_proveedor, form_del_insumo

urlpatterns = [
    path('', inicio,name="inicio"),
    path('proveedor', proveedor,name="proveedor"),
    path('insumo', insumo,name="insumo"),
    path('form-proveedor',form_proveedor,name='form_proveedor'),
    path('form-insumo',form_insumo,name='form_insumo'),
    path('form-mod-insumo/<id>',form_mod_insumo,name='form_mod_insumo'),
    path('form-mod-proveedor/<id>',form_mod_proveedor,name='form_mod_proveedor'),
    path('form-del-proveedor/<id>', form_del_proveedor, name="form_del_proveedor"),
    path('form-del-insumo/<id>', form_del_insumo, name="form_del_insumo")
]