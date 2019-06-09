"""URLs da aplicação avisos."""

from django import urls

from . import views

app_name = 'avisos'

urlpatterns = [
    urls.re_path(r'^partials/aviso/$', views.aviso_partial_view, name='aviso_partial_view'),
    urls.re_path(r'^partials/avisos/$', views.avisos_partial_view, name='avisos_partial_view'),
]
