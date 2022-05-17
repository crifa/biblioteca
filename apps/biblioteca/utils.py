import datetime
import json

import requests
from django.core import serializers
from django.db.models import Q

from .models import Libro, Autor, Categoria, Editor


class Biblioteca():
    google_url = 'https://www.googleapis.com/books/v1/volumes?q='

    def buscar_libro(self, query):
        libros = Libro.objects.filter(Q(titulo__icontains=query) |
                                      Q(identificador__icontains=query) |
                                      Q(descripcion__icontains=query) |
                                      Q(subtitulo__icontains=query) |
                                      Q(fecha_publicacion__icontains=query) |
                                      Q(autor__nombre__icontains=query) |
                                      Q(editor__nombre__icontains=query) |
                                      Q(categoria__nombre__icontains=query)
        ).distinct()
        lista_libros = []
        if libros:
            resultado = serializers.serialize("json", libros)
        else:
            resultado = self.buscar_libro_google(query)
        return resultado

    def buscar_libro_google(self, query):
        libro = query.replace(" ", '+')
        url = self.google_url+libro
        response = requests.get(url)
        data = response.json()
        items = data["items"]
        encoded = json.dumps(items)
        decoded = json.loads(encoded)
        #print("decoded: ", decoded)
        return decoded

    def guardar_libro(self, identificador, proveedor):
        print("provvedor: ", proveedor)
        if proveedor == 'google':
            self.guardar_libro_google(identificador)

    def guardar_libro_google(self, identificador):
        resultado = self.buscar_libro_google(identificador)
        for libro in resultado:
            print("libro id ", libro['id'])

            try:
                subtitulo = libro['volumeInfo']['subtitle']
            except:
                subtitulo = ''

            try:
                descripcion = libro['volumeInfo']['descripcion']
            except:
                descripcion = ''

            try:
                if isinstance(libro['volumeInfo']['publishedDate'], datetime.date):
                    publishedDate = libro['volumeInfo']['publishedDate']
                else:
                    raise Exception
            except:
                publishedDate = None

            try:
                categorias = libro['volumeInfo']['categories']
            except:
                categorias = []

            try:
                autores = libro['volumeInfo']['authors']
            except:
                autores = []

            try:
                publicador = libro['volumeInfo']['publisher']
            except:
                publicador = 'Sin editor'

            self.guardar_libro_bd(libro['id'],
                                  libro['volumeInfo']['title'],
                                  subtitulo,
                                  descripcion,
                                  publishedDate,
                                  autores,
                                  publicador,
                                  categorias,
                                  libro['volumeInfo']['imageLinks']['smallThumbnail']
                                  )
        return 'succes'

    def guardar_libro_bd(self, identificador, titulo, subtitulo, descripcion, fecha_publicacion,
                         autores, editor, categorias, imagen=''):
        n_editor = Editor(nombre=editor)
        n_editor.save()
        nuevo_libro = Libro(
            identificador=identificador,
            titulo=titulo,
            subtitulo=subtitulo,
            descripcion=descripcion,
            fecha_publicacion=fecha_publicacion,
            imagen=imagen,
            editor=n_editor
        )
        nuevo_libro.save()
        for autor in autores:
            autor_n = Autor(nombre=autor)
            autor_n.save()
            nuevo_libro.autor.add(autor_n)
            nuevo_libro.save()

        for categoria in categorias:
            print("categoria: ", categoria)
            categoria_n = Categoria(nombre=categoria)
            categoria_n.save()
            nuevo_libro.categoria.add(categoria_n)
            nuevo_libro.save()

    def eliminar_libro(self):
        pass


