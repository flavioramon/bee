"""Fábricas da aplicação abelhas."""

import random

import factory

from . import models


class TipoAbelhaFactory(factory.DjangoModelFactory):
    """Fábrica para tipos de abelhas."""

    @factory.lazy_attribute
    def nome(self):
        """Nome aleatório."""
        return random.choice(['Com Ferrão', 'Sem Ferrão'])

    class Meta:
        """Meta opções da fábrica."""

        model = models.TipoAbelha
        django_get_or_create = ('nome',)


class EspecieAbelhaFactory(factory.DjangoModelFactory):
    """Fábrica para tipos de abelhas."""

    @factory.lazy_attribute
    def nome(self):
        """Nome aleatório."""
        return random.choice([
            'Abelha Europeia',
            'Abelha Asiática',
            'Abelha Asiática Anã',
            'Abelha Gigante',
            'Abelha das Filipinas',
            'Abelha de Koschevnikov',
            'Abelha Preta Asiática Anã',
            'Apis armbrusteri',
            'Apis lithohermaea',
            'Apis nearctica'
        ])

    class Meta:
        """Meta opções da fábrica."""

        model = models.EspecieAbelha
        django_get_or_create = ('nome',)


class PaisAbelhaFactory(factory.DjangoModelFactory):
    """Fábrica para tipos de abelhas."""

    @factory.lazy_attribute
    def nome(self):
        """Nome aleatório."""
        return random.choice([
            'Argentina',
            'Brasil',
            'Japão',
            'Noruega',
        ])

    class Meta:
        """Meta opções da fábrica."""

        model = models.PaisAbelha
        django_get_or_create = ('nome',)


class AbelhaFactory(factory.DjangoModelFactory):
    """Fábrica para tipos de abelhas."""

    especie = factory.SubFactory(EspecieAbelhaFactory)
    tipo = factory.SubFactory(TipoAbelhaFactory)
    pais = factory.SubFactory(PaisAbelhaFactory)

    @factory.lazy_attribute
    def codigo(self):
        """Código aleatório."""
        return '0D011020'

    @factory.lazy_attribute
    def numero(self):
        """Número aleatório."""
        return random.randint(10000, 1000000)

    class Meta:
        """Meta opções da fábrica."""

        model = models.Abelha
