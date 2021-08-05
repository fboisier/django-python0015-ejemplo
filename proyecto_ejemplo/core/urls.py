from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index , name = 'inicio'),    
    path('resetea/', views.resetear, name = 'reiniciar'),
    path('tiempo/', views.tiempo, name = 'tiempo'),
    path('procesar/<str:opcion>', views.procesar, name="procesar"),

    path('ejemplo1/', views.ejemplo),
    path('crear-datos/', views.crear_datos),
    path('vaciar-datos/', views.vaciar_datos),
]
