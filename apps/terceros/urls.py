from django.urls import include,path
from rest_framework.routers import DefaultRouter

from .views import TerceroViewSet,ReferenciaViewSet



router = DefaultRouter()
router.register("terceros", TerceroViewSet)
router.register("referencia", ReferenciaViewSet)



urlpatterns = [
    path("", include(router.urls)),
  
]

urlpatterns += router.urls

