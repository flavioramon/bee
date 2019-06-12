"""Api da aplicação leituras."""

import csv

from django.core.files import base
from rest_framework import decorators, response, serializers, status, viewsets

from core.pagination import CorePaginator

from . import fields, models


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


class LeituraViewSet(viewsets.ModelViewSet):
    """Conjunto de views para leituras."""

    serializer_class = LeituraSerializer
    queryset = models.Leitura.objects.all()
    pagination_class = CorePaginator

    @decorators.action(detail=False, methods=['POST'])
    def processar_arquivo(self, request, pk=None):
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

        except Exception:
            mensagem = 'Ocorreu um erro ao processar o arquivo.'
            return response.Response(mensagem, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
