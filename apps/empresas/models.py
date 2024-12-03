from django.db import models


class Empresa(models.Model):
    nombre  = models.CharField(max_length=255)
    nit     = models.CharField(max_length=255)  
    direccion   = models.CharField(max_length=255,blank=True, null=True)     
    contacto    =  models.CharField(max_length=255,blank=True, null=True)   
    telefono    =  models.CharField(max_length=255,blank=True, null=True)   
    email       =  models.EmailField(max_length=255)   
    create_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    