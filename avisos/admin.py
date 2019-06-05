"""Administração da aplicação avisos."""

from django.contrib import admin

from . import models


@admin.register(models.Aviso)
class AvisoAdmin(admin.ModelAdmin):
    """Administração de avisos."""
