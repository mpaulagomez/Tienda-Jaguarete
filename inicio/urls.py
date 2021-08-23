from django.urls import path
from .views import Contacto, Inicio, AcercaDe, Gracias

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('Acerca de', AcercaDe.as_view(), name='acercade'),
    path('Gracias', Gracias.as_view(), name='gracias' ),
    path('Contacto', Contacto.as_view(), name='contacto'),
    
]
