from django.urls import path
from .views import *

urlpatterns = [
    path('mostrar/', mostrar_lab, name='mostrar-lab'),
    path('crear/', insertar_lab, name='insertar-lab'),
    path('editar/<int:pk>', editar_lab, name='editar-lab'),
    path('editar/actualizarlaboratorio/<int:id>', actualizarlaboratorio, name='actualizarlaboratorio'),
    path('eliminar/<int:pk>', eliminar_lab, name='eliminar-lab'),
]