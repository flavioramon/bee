"""Gerenciadores da aplicação leituras."""

from django.db import models


class LeituraManager(models.Manager):
    """Gerenciador de leituras."""

    def gerar_avisos(self, dia):
        """Gera avisos em função de dados de leituras."""
