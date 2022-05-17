from django.urls import path

from .views import BibliotecaView

views_urls_biblioteca = [
    path('', BibliotecaView.as_view(), name='biblioteca_buscar'),
]