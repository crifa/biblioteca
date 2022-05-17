from django.db import models

# Create your models here.
'''
● Id
● Título
● Subtítulo
● Autor(es)
● Categoría(s)
● Fecha publicación
● 1 Editor
● Descripción
● Imagen (Opcional)
'''


class Editor(models.Model):
    nombre = models.CharField(max_length=300)


class Autor(models.Model):
    nombre = models.CharField(max_length=300)


class Categoria(models.Model):
    nombre = models.CharField(max_length=300)


class Libro(models.Model):
    identificador = models.CharField(max_length=300)
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField()
    subtitulo = models.CharField(max_length=300)
    autor = models.ManyToManyField(Autor, blank=True)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria, blank=True)
    imagen = models.URLField(blank=True, null=True)
    fecha_publicacion = models.DateField(blank=True, null=True)




