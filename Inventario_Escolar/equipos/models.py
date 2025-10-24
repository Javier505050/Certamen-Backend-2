from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(choices=[("proyector","Proyector"),("Notebook", "Impresora")], max_length=50) 
    estado = models.CharField(choices=[("operativo","Operativo"),("en reparacion", "En Reparacion"),("dado de baja", "Dado de Baja")], default="operativo")
    ubicacion = models.TextField(choices=[("sala de profesores","Sala de Profesores"),("biblioteca", "Biblioteca"),("sala de computacion", "Sala de Computacion")], max_length=100)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre