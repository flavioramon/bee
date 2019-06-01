"""Administração da aplicação abelhas."""

from django.contrib import admin

from . import models


@admin.register(models.TipoAbelha)
class TipoAbelhaAdmin(admin.ModelAdmin):
    """Adminitração de tipos de abelhas."""


@admin.register(models.EspecieAbelha)
class EspecieAbelhaAdmin(admin.ModelAdmin):
    """Adminitração de tipos de abelhas."""


@admin.register(models.PaisAbelha)
class PaisAbelhaAdmin(admin.ModelAdmin):
    """Adminitração de tipos de abelhas."""


@admin.register(models.Abelha)
class AbelhaAdmin(admin.ModelAdmin):
    """Adminitração de tipos de abelhas."""
