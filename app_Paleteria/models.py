from django.db import models

# MODELO: PROVEEDOR
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100, unique=True)
    contacto = models.CharField(max_length=100, blank=True)   # no hace falta unique en contacto
    telefono = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)      # auto ahora
    ciudad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre_empresa

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    sabor = models.CharField(max_length=100, unique=True)
    precio = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha_elaboracion = models.CharField(max_length=100)
    id_proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, db_column='id_proveedor', related_name='productos'
    )

    def __str__(self):
        return f"{self.nombre} ({self.sabor})"