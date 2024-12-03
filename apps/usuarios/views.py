from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from apps.usuarios.UserLoginSerializer import UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuariosViewSet(ModelViewSet):
    queryset = Usuario.objects.all()  
    serializer_class = UsuarioSerializer

    def retrieve(self, request, pk=None):
        usuario = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioSerializer(usuario)  
        return Response(serializer.data)

class UsuarioLoginAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        try:           
            refresh_token = request.data["refresh"]           
            token = RefreshToken(refresh_token)
            token.blacklist()            
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)                      
        except Exception as e:
            return Response({"message": str(e)}, status=400)