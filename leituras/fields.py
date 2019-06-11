"""Campos da aplicação leituras."""

from drf_extra_fields import fields


class CSVBase64FileField(fields.Base64FileField):
    """Arquivo Base64 CSV contendo dados de leitura."""

    @property
    def ALLOWED_TYPES(self):
        """Obtém a lista de extensões permitidas."""
        return ['csv']

    def get_file_extension(self, filename, decoded_file):
        """Obtém a extensão do arquivo."""
        return 'csv'
