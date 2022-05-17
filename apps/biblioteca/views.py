import requests
import json

# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Autor
from .utils import Biblioteca

biblioteca = Biblioteca()

class BibliotecaView(APIView):

    def get(self, request):
        libro = request.GET.get('libro')
        print("el libro es: ", libro)
        resultado = biblioteca.buscar_libro(libro)
        return JsonResponse(data={'response':resultado})

    def post(self, request):
        print("entro en post")
        id = request.POST.get('id')
        fuente = request.POST.get('fuente')
        resultado = biblioteca.guardar_libro(id, fuente)
        return JsonResponse(data={'response':resultado})

