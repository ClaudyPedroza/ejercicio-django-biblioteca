from django.contrib import admin
from .models import Autor,Libro,Resena

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    #list_display:nos permite elegir que campos del modelo quieres ver como columnas en la tabla del admin
    list_display = ('nombre', 'nacionalidad')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'resumen')
    search_fields = ('titulo', 'autor__nombre')
    list_filter = ['autor']

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'calificacion', 'fecha')

