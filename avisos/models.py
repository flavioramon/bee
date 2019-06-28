"""Modelos da aplicação avisos."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from model_utils.models import TimeStampedModel


class Aviso(TimeStampedModel):
    """Representa um aviso no sistema."""

    codigo = models.CharField(max_length=255)
    descricao = models.TextField()
    dia = models.DateField()

    historico = AuditlogHistoryField()

    def __str__(self):
        """toString."""
        return self.codigo


auditlog.register(Aviso)
