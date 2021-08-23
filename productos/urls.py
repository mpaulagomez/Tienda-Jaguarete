from django.urls import path
from .views import Remeras, Camperas, Pantalones, Zapatillas, Medias, ProductoDetalle, Busqueda, CrearProducto, EditarProducto, EliminarProducto
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('remeras', Remeras.as_view(), name='remeras'),
    path('camperas', Camperas.as_view(), name='camperas'),
    path('pantalones', Pantalones.as_view(), name='pantalones'),
    path('zapatillas', Zapatillas.as_view(), name='zapatillas'),
    path('medias', Medias.as_view(), name='medias'),
    path('producto/<int:pk>/', ProductoDetalle.as_view(), name='detalle'),
    path('resultados', Busqueda.as_view(), name='resultados'),
    path('nuevo', CrearProducto.as_view(), name='nuevo'),
    path('producto/<int:pk>/editar', EditarProducto.as_view(), name='editar'),
    path('producto/<int:pk>/borrar', EliminarProducto.as_view(), name='borrar'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)