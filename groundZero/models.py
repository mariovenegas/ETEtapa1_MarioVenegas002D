from django.db import models

# Create your models here.

#Modelo para Pais
class Pais(models.Model):
    idPais =models.IntegerField(primary_key=True, verbose_name='Identificacion del pais')
    nombre = models.CharField(max_length=20, verbose_name='Nombre del Pais')

    def __str__(self):
        return self.nombre

#Modelo para Proveedor
class Proveedor(models.Model):
    numeroIdentificacion =models.IntegerField(primary_key=True, verbose_name='Identificacion del proveedor')
    nombre =models.CharField(max_length=50, verbose_name='Nombre del proveedor')
    telefono = models.CharField(max_length=20, verbose_name='Telefono del proveedor')
    direccion = models.CharField(max_length=50, verbose_name='Direccion del proveedor')
    email = models.CharField(max_length=50, verbose_name='Email del proveedor')
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    clave = models.CharField(max_length=8, verbose_name='Clave del proveedor')
    moneda = models.CharField(max_length=10, verbose_name='Clave del proveedor')
    
    def __str__(self):
        return self.nombre

#Modelo para Insumos
class Insumo(models.Model):
    idInsumo =models.IntegerField(primary_key=True, verbose_name='Identificacion del insumo')
    nombre =models.CharField(max_length=20, verbose_name='Nombre del insumo')
    descripcion =models.CharField(max_length=50, verbose_name='Descripcion del insumo')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
