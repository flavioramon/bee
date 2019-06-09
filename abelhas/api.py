"""Api da aplicação abelhas."""

from rest_framework import permissions, serializers, viewsets

from core.pagination import CorePaginator

from . import models


class TipoAbelhaSerializer(serializers.ModelSerializer):
    """Serializador de tipos de abelhas."""

    class Meta:
        """Meta opções do serializador."""

        model = models.TipoAbelha
        fields = '__all__'


class EspecieAbelhaSerializer(serializers.ModelSerializer):
    """Serializador de espécies de abelhas."""

    class Meta:
        """Meta opções do serializador."""

        model = models.EspecieAbelha
        fields = '__all__'


class PaisAbelhaSerializer(serializers.ModelSerializer):
    """Serializador de países de abelhas."""

    class Meta:
        """Meta opções do serializador."""

        model = models.PaisAbelha
        fields = '__all__'


class AbelhaSerializer(serializers.ModelSerializer):
    """Serializador de abelhas."""

    tipo_data = TipoAbelhaSerializer(source='tipo', read_only=True)
    especie_data = EspecieAbelhaSerializer(source='especie', read_only=True)
    pais_data = PaisAbelhaSerializer(source='pais', read_only=True)

    class Meta:
        """Meta opções do serializador."""

        model = models.Abelha
        fields = '__all__'


class AbelhaViewSet(viewsets.ModelViewSet):
    """Conjunto de views para abelhas."""

    serializer_class = AbelhaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CorePaginator
    queryset = models.Abelha.objects.all()
    search_fields = ['codigo', 'numero', 'especie__nome', 'tipo__nome', 'pais__nome']


class EspecieAbelhaViewSet(viewsets.ModelViewSet):
    """Conjunto de views para especies."""

    serializer_class = EspecieAbelhaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CorePaginator
    queryset = models.EspecieAbelha.objects.all()
    search_fields = ['id', 'nome']


class TipoAbelhaViewSet(viewsets.ModelViewSet):
    """Conjunto de views para tipos de abelhas."""

    serializer_class = TipoAbelhaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CorePaginator
    queryset = models.TipoAbelha.objects.all()
    search_fields = ['id', 'nome']


class PaisAbelhaViewSet(viewsets.ModelViewSet):
    """Conjunto de views para Paiss de abelhas."""

    serializer_class = PaisAbelhaSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CorePaginator
    queryset = models.PaisAbelha.objects.all()
    search_fields = ['id', 'nome']
