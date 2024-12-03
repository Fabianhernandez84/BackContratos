from django.db import models
from apps.empresas.models import Empresa
from apps.terceros.models import Tercero



class estadoContrato(models.Model):
    nombre      = models.CharField(max_length=255)
    descipcion  = models.CharField(max_length=255)

class Contrato(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField() 
    fecha_fin = models.DateField() 
    lugar = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    documento = models.FileField(upload_to="contratos",blank=True,null=True)    
    contratante     = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    cliente         = models.ForeignKey(Tercero,on_delete=models.CASCADE )
    valor_contrato  = models.DecimalField(max_digits=10, decimal_places=2)        
    estado          = models.ForeignKey(estadoContrato,on_delete=models.CASCADE)
    create_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    