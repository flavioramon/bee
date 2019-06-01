"""Modelos da aplicação abelhas."""

from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from django.db import models
from model_utils.models import TimeStampedModel


class TipoAbelha(TimeStampedModel):
    """Representa um tipo de abelha."""

    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    historico = AuditlogHistoryField()

    def __str__(self):
        """Representação textual do objeto."""
        return self.nome


auditlog.register(TipoAbelha)


class EspecieAbelha(TimeStampedModel):
    """Representa uma espécie de abelha."""

    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    historico = AuditlogHistoryField()

    def __str__(self):
        """Representação textual do objeto."""
        return self.nome


auditlog.register(EspecieAbelha)


class PaisAbelha(TimeStampedModel):
    """Representa um país de origem de uma abelha."""

    nome = models.CharField(max_length=100)

    historico = AuditlogHistoryField()

    def __str__(self):
        """Representação textual do objeto."""
        return self.nome


auditlog.register(PaisAbelha)


class Abelha(TimeStampedModel):
    """Representa uma abelha."""

    especie = models.ForeignKey(EspecieAbelha, related_name='abelhas', on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoAbelha, related_name='abelhas', on_delete=models.CASCADE)
    pais = models.ForeignKey(PaisAbelha, related_name='abelhas', on_delete=models.CASCADE)

    codigo = models.CharField(max_length=100)
    numero = models.IntegerField()

    historico = AuditlogHistoryField()


auditlog.register(Abelha)
