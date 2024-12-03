from django.db import models
from apps.usuarios.models import Usuario

class Tercero(models.Model):
    nombre              = models.CharField(max_length=255)
    identificacion      = models.CharField(max_length=255,unique=True)  
    direccion           = models.CharField(max_length=255,blank=True, null=True)     
    contacto            =  models.CharField(max_length=255,blank=True, null=True)   
    telefono            =  models.CharField(max_length=255,blank=True, null=True)   
    ocupacion           =  models.CharField(max_length=255,blank=True, null=True)   
    email               =  models.EmailField(max_length=255)  
    ingresos            = models.DecimalField(max_digits=10, decimal_places=2)     
    cedula              = models.FileField(upload_to="cedulas/",blank=True, null=True)  
    certificado_laboral = models.FileField(upload_to="certificados/",blank=True, null=True) 
    Usuario             = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank=True, null=True )
    create_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 


class Referencia(models.Model):
    tercero = models.ForeignKey(Tercero,on_delete=models.CASCADE)
    nombre  = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255) 
    email       =  models.EmailField(max_length=255)  
    create_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
   