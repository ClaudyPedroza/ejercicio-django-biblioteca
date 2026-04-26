from django.db import models
from django.core.exceptions import ValidationError

def validar_nombre(value):
    if not value.strip():
        raise ValidationError("El nombre no puede estar vacio o tener solo espacios")
    
def validar_resumen(value):
    if len(value)<50:
        raise ValidationError("El resumen debe tener al menos 50 caracteres")
    
def validar_resena(value):
    if value < 1 or value > 5:
        raise ValidationError("La calificacion debe estar entre el rango 1-5")
        

class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre])
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validar_resumen])

    def __str__(self):
        return self.titulo
    
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE,related_name='resenas')
    texto = models.TextField()
    calificacion = models.IntegerField(validators=[validar_resena])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"
