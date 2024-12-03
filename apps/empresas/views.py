from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Empresa
from .serializers import EmpresaSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class EmpresaAPIView(APIView):
   
    def get(self, request, format=None):        
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)        
        return Response(serializer.data)
    
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
    def post(self, request):   
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):    
        empresa = get_object_or_404(Empresa, pk=pk)
        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):     
        empresa = get_object_or_404(Empresa, pk=pk)
        empresa.delete()
        return Response({'mensaje': 'Empresa eliminada exitosamente.'}, status=status.HTTP_204_NO_CONTENT)