"""Api da aplicação leituras."""

import csv
import logging

from django.core.files import base
from rest_framework import decorators, response, serializers, status, viewsets, permissions

from core.pagination import CorePaginator

from . import fields, models


logger = logging.getLogger(__name__)


class ProcessarArquivoSerializer(serializers.Serializer):
    """Serializador para arquivos enviados."""

    arquivo = fields.CSVBase64FileField()

    def converter_arquivo(self):
        """Converte um arquivo binário csv em um dicionário de dados."""  # noqa: D401
        arquivo = self.validated_data['arquivo']
        arquivo = base.ContentFile(arquivo.file.read().decode('utf-8'))
        return list(csv.DictReader(arquivo))

    def preparar_dados(self, dados):
        """Normaliza dados para serem utilizados pelo serializador."""
        for dado in dados:
            # adiciona zeros para ajustar o timezone de forma a corresponder com input_formats.
            reading_time_local = dado['reading_time_local']
            dado['reading_time_local'] = reading_time_local + '0' * (27 - len(reading_time_local))


class LeituraSerializer(serializers.ModelSerializer):
    """Serializador de leituras."""

    reading_time_local = serializers.DateTimeField(
        input_formats=['%Y%m%dT%H%M%S.%f%z']
    )

    class Meta:
        """Meta opções do serializador."""

        model = models.Leitura
        fields = '__all__'

    def create(self, validated_data):
        """Idempotent create, baseado em reading_time_local e bee_id."""
        reading_time_local = validated_data.pop('reading_time_local')
        bee_id = validated_data.pop('bee_id')
        leitura, criado = models.Leitura.objects.update_or_create(
            reading_time_local=reading_time_local,
            bee_id=bee_id,
            defaults=validated_data
        )
        return leitura


class LeituraViewSet(viewsets.ModelViewSet):
    """Conjunto de views para leituras."""

    serializer_class = LeituraSerializer
    queryset = models.Leitura.objects.all()
    pagination_class = CorePaginator

    @decorators.action(detail=False, methods=['post'])
    def processar_arquivo(self, request):
        """Processa o arquivo de leitura csv."""
        try:
            serializer = ProcessarArquivoSerializer(data=request.data)
            if serializer.is_valid():
                dados = serializer.converter_arquivo()
                serializer.preparar_dados(dados)
                serializer = self.get_serializer(data=dados, many=True)
                if serializer.is_valid():
                    serializer.save()
                    mensagem = 'Arquivo processado com sucesso'
                    return response.Response(mensagem, status=status.HTTP_201_CREATED)

            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(e)
            mensagem = 'Ocorreu um erro ao processar o arquivo.'
            return response.Response(mensagem, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @decorators.action(detail=False, methods=['delete'], permission_classes=[permissions.IsAdminUser])
    def deletar_leituras(self, request):
        """Remove todas as leituras de uma vez. Útil para testar a idempotência do upload de arquivos."""
        models.Leitura.objects.all().delete()
        return response.Response('Leituras removidas com sucesso.', status=status.HTTP_200_OK)
