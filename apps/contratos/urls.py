from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .views import ContratosViewSet,EstadoContratoViewSet


router = DefaultRouter()
router.register("contratos", ContratosViewSet)
router.register("estado-contratos", EstadoContratoViewSet)



urlpatterns = [
    path("", include(router.urls)),
  
]

urlpatterns += router.urls

