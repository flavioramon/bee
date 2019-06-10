"""Api da aplicação leituras."""

from rest_framework import decorators, serializers, viewsets

from . import models


class LeituraSerializer(serializers.ModelSerializer):
    """Serializador de leituras."""

    class Meta:
        """Meta opções do serializador."""

        model = models.Leitura
        fields = '__all__'


class LeituraViewSet(viewsets.ModelViewSet):
    """Conjunto de views para leituras."""

    serializer_class = LeituraSerializer
    queryset = models.Leitura.objects.all()

    @decorators.action(detail=False, methods=['POST'])
    def processar_arquivo(self, request, pk=None):
        """Processa o arquivo de leitura csv."""
