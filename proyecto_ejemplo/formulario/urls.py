from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario),    
    path('resultado/', views.resultado),    
]
