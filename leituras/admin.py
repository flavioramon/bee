"""Administração da aplicação leituras."""

from django.contrib import admin

from . import models


@admin.register(models.Leitura)
class LeituraAdmin(admin.ModelAdmin):
    """Leitura admin."""
