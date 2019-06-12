"""URLs da aplicação leituras."""

from django import urls

from . import views

urlpatterns = [
    urls.re_path(r'^processar/arquivo/$', views.processar_arquivo, name='processar_arquivo'),
    urls.re_path(r'^lista/$', views.leituras_lista, name='leituras_lista'),
]
