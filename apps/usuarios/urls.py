from django.urls import include,path
from rest_framework.routers import DefaultRouter

from apps.usuarios.views import UsuariosViewSet,UsuarioLoginAPIView,LogoutView
from rest_framework_simplejwt.views import TokenVerifyView



router = DefaultRouter()
router.register("usuarios", UsuariosViewSet)




urlpatterns = [
    path('login-auth/', UsuarioLoginAPIView.as_view(), name='login-auth'),
    path('auth-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout-auth/', LogoutView.as_view(), name='logout-auth'),
    path('api-usuarios/', LogoutView.as_view(), name='logout-auth'),
    path("", include(router.urls)),
  
    
]

urlpatterns += router.urls