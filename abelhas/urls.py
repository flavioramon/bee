"""URLs da aplicação abelhas."""

from django import urls

from . import views

app_name = 'abelhas'

urlpatterns = [
    urls.re_path(r'^partials/abelha/$', views.abelha_partial_view, name='abelha_partial_view'),
    urls.re_path(r'^partials/abelhas/$', views.abelhas_partial_view, name='abelhas_partial_view'),
]
