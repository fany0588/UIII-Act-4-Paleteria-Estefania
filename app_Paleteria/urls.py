from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_paleteria, name='inicio_paleteria'),

    # --- PROVEEDOR ---
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/ver/', views.ver_proveedor, name='ver_proveedor'),
    path('proveedor/editar/<int:pk>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/editar/realizar/<int:pk>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedor/borrar/<int:pk>/', views.borrar_proveedor, name='borrar_proveedor'),

    # --- PRODUCTO ---
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/ver/', views.ver_producto, name='ver_producto'),
    path('producto/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),
]
