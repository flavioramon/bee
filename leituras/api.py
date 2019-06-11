"""Api da aplicação leituras."""

import csv

from django.core.files import base
from rest_framework import decorators, exceptions, response, serializers, status, viewsets

from . import fields, models


class ProcessarArquivoSerializer(serializers.Serializer):
    """Serializador para arquivos enviados."""

    arquivo = fields.CSVBase64FileField()


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

    def converter_arquivo(self, arquivo):
        """Converte um arquivo binário csv em um dicionário de dados."""  # noqa: D401
        arquivo = base.ContentFile(arquivo.file.read().decode('utf-8'))
        return list(csv.DictReader(arquivo))

    def preparar_dados(self, dados):
        """Normaliza dados para serem utilizados pelo serializador."""
        for dado in dados:
            # adiciona zeros para ajustar o timezone de forma a corresponder com input_formats.
            reading_time_local = dado['reading_time_local']
            dado['reading_time_local'] = reading_time_local + '0' * (27 - len(reading_time_local))

    @decorators.action(detail=False, methods=['POST'])
    def processar_arquivo(self, request, pk=None):
        """Processa o arquivo de leitura csv."""
        try:
            serializer = ProcessarArquivoSerializer(data=request.data)
            if serializer.is_valid():
                dados = self.converter_arquivo(serializer.validated_data['arquivo'])
                self.preparar_dados(dados)
                serializer = self.get_serializer(data=dados, many=True)
                if serializer.is_valid():
                    for validated_data in serializer.validated_data:
                        models.Leitura.objects.create(**validated_data)

                    data = dict(mensagem='Arquivo processado com sucesso')
                    return response.Response(data, status=status.HTTP_201_CREATED)

                else:
                    raise exceptions.ValidationError()

            else:
                raise exceptions.ValidationError()

        except exceptions.ValidationError:
            return response.Response(serializer.errors[0], status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            data = dict(mensagem=str(e))
            return response.Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
