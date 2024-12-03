from django.urls import path
from .views import EmpresaAPIView

urlpatterns = [
    path('empresa/', EmpresaAPIView.as_view()),
    path('empresa/<int:pk>/', EmpresaAPIView.as_view()),
]