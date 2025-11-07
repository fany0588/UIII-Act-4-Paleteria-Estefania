from django.contrib import admin
from .models import Proveedor, Producto

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre_empresa', 'contacto', 'telefono', 'email', 'ciudad', 'fecha_registro')
    search_fields = ('nombre_empresa', 'contacto', 'ciudad')

admin.site.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'sabor', 'precio', 'stock', 'tipo', 'fecha_elaboracion', 'id_proveedor')
    search_fields = ('nombre', 'sabor', 'tipo')
    