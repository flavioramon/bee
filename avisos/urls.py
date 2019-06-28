"""URLs da aplicação avisos."""

from django import urls

from . import views

app_name = 'avisos'

urlpatterns = [
    urls.re_path(r'^lista/$', views.aviso_lista_view, name='aviso_lista_view'),
]
