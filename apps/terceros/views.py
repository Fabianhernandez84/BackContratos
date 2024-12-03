from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status,generics
from django.shortcuts import get_object_or_404
from .models import Tercero, Referencia
from .serializers import TerceroSerializer, ReferenciaSerializer
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi





class TerceroViewSet(ModelViewSet):
    queryset = Tercero.objects.all()  
    serializer_class = TerceroSerializer

    
    @swagger_auto_schema(
        operation_description="Crear un nuevo Tercero",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'nombre': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre del Tercero'),
                'identificacion': openapi.Schema(type=openapi.TYPE_STRING, description='Identificación única'),
            },
            required=['nombre', 'identificacion']
        ),
        responses={201: 'Tercero creado exitosamente', 400: 'Error en la solicitud'}
    )
    def create(self, request,*args, **kwargs):   
        
        datos = request.data.copy()
        cedula              = request.FILES.get('cedula')
        certificado_laboral = request.FILES.get('certificado_laboral')
        if cedula :
            datos['cedula'] = cedula
        if certificado_laboral:
            datos['certificado_laboral'] = request.FILES.get('certificado_laboral')
        
        serializer = TerceroSerializer(data=datos)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        tercero = get_object_or_404(Tercero, pk=pk)
        serializer = TerceroSerializer(tercero)  
        return Response(serializer.data)

    def update(self, request, pk):    
        tercero = get_object_or_404(Tercero, pk=pk)

        datos = request.data.copy()
        cedula              = request.FILES.get('cedula')
        certificado_laboral = request.FILES.get('certificado_laboral')
        if cedula :
            datos['cedula'] = cedula
        if certificado_laboral:
            datos['certificado_laboral'] = request.FILES.get('certificado_laboral')        

        serializer = TerceroSerializer(tercero, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):     
        tercero = get_object_or_404(Tercero, pk=pk)
        tercero.delete()
        return Response({'mensaje': 'Tercero eliminado exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=["POST"], url_path="referencias")
    def referencias(self, request):     
        data = request.data
        tercero_id = data["tercero"]
        tercero = get_object_or_404(Tercero, pk=tercero_id)
        referecia = Referencia.objects.filter(tercero=tercero)
       
       # Serializamos las referencias
        serializer = ReferenciaSerializer(referecia, many=True)        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ReferenciaViewSet(ModelViewSet):
    queryset = Referencia.objects.all()  
    serializer_class = ReferenciaSerializer
    
    
    @swagger_auto_schema(
        operation_description="Crear un nuevo Tercero",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'tercero': openapi.Schema(type=openapi.TYPE_STRING, description='ID del Tercero'),
                'nombre': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre Referencia'),
                'identificacion': openapi.Schema(type=openapi.TYPE_STRING, description='Identificación Referencia'),
                'telefono': openapi.Schema(type=openapi.TYPE_STRING, description='telefono Referencia'),
                'direccion': openapi.Schema(type=openapi.TYPE_STRING, description='direccion Referencia'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email referencia'),
            },
            required=['tercero','nombre', 'identificacion','telefono','direccion','email']
        ),
        responses={201: 'Tercero creado exitosamente', 400: 'Error en la solicitud'}
    )
    def create(self, request):   
        serializer = ReferenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        referencia = get_object_or_404(Referencia, pk=pk)
        serializer = TerceroSerializer(referencia)  
        return Response(serializer.data)
    
    def update(self, request, pk):    
        referencia = get_object_or_404(Referencia, pk=pk)
        serializer = ReferenciaSerializer(referencia, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):     
        referencia = get_object_or_404(Referencia, pk=pk)
        referencia.delete()
        return Response({'mensaje': 'Referencia de contrato eliminado exitosamente.'}, status=status.HTTP_204_NO_CONTENT)