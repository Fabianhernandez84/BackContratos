from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Contrato,estadoContrato
from .serializers import ContratosSerializer,ContratosResponseSerializer,EstadosContratoSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ContratosViewSet(ModelViewSet):
    queryset = Contrato.objects.all()  
    serializer_class = ContratosResponseSerializer

        
    @swagger_auto_schema(
        operation_description="Crear un nuevo contrato",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nombre': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre del contrato'),
                'fecha_inicio': openapi.Schema(type=openapi.TYPE_STRING, description='fecha de inicio del contrato'),
            },
            required=['nombre', 'fecha_inicio']
        ),
        responses={201: 'Contrato creado exitosamente', 400: 'Error en la solicitud'}
    )
    def create(self, request):   
        serializer = ContratosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        contrato = get_object_or_404(Contrato, pk=pk)
        serializer = ContratosSerializer(contrato)  
        return Response(serializer.data)
    
    def update(self, request, pk):    
        contrato = get_object_or_404(Contrato, pk=pk)
        serializer = ContratosSerializer(contrato, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):     
        contrato = get_object_or_404(Contrato, pk=pk)
        contrato.delete()
        return Response({'mensaje': 'Contrato eliminado exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
    


class EstadoContratoViewSet(ModelViewSet):
    queryset = estadoContrato.objects.all()  
    serializer_class = EstadosContratoSerializer


   
    @swagger_auto_schema(
        operation_description="Crear un nuevo estado de contrato",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nombre': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre del estad'),
                'descipcion': openapi.Schema(type=openapi.TYPE_STRING, description='descipcion del estado'),
            },
            required=['nombre', 'descipcion']
        ),
        responses={201: 'Estado creado exitosamente', 400: 'Error en la solicitud'}
    )
    def create(self, request):   
        serializer = EstadosContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        estados = get_object_or_404(estadoContrato, pk=pk)
        serializer = EstadosContratoSerializer(estados)  
        return Response(serializer.data)
    
    def update(self, request, pk):    
        estados = get_object_or_404(estadoContrato, pk=pk)
        serializer = EstadosContratoSerializer(estados, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):     
        estados = get_object_or_404(estadoContrato, pk=pk)
        estados.delete()
        return Response({'mensaje': 'Estado de contrato eliminado exitosamente.'}, status=status.HTTP_204_NO_CONTENT)