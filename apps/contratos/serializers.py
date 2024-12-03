from rest_framework import serializers
from .models import Contrato,estadoContrato
from apps.terceros.serializers import TerceroSerializer 


class ContratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = (
            'id',
            'nombre',
            'fecha_inicio',
            'fecha_fin',
            'lugar',           
            'descripcion',  
            'documento', 
            'contratante',
            'cliente',
            'estado',
            'valor_contrato'
        )

class EstadosContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = estadoContrato
        fields = (
            'id',
            'nombre',            
        )

class ContratosResponseSerializer(serializers.ModelSerializer):
    cliente = TerceroSerializer(read_only=True)
    estado  = EstadosContratoSerializer(read_only=True)

    class Meta:
        model = Contrato
        fields = (
            'id',
            'nombre',
            'fecha_inicio',
            'fecha_fin',
            'lugar',           
            'descripcion',  
            'documento', 
            'contratante',
            'cliente',
            'estado',
            'valor_contrato'
        )


