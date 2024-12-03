from rest_framework import serializers
from .models import Tercero, Referencia

class TerceroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tercero
        fields = (
            'id',
            'nombre',
            'identificacion',
            'direccion',
            'contacto',           
            'telefono',   
            'ocupacion',
            'cedula',
            'certificado_laboral',
            'email',
            'ingresos'
        )

class ReferenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Referencia
        fields = (
            'id',
            'tercero',
            'nombre',
            'identificacion',
            'telefono',   
            'direccion',
            'email',
        )
