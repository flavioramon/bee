"""Api da aplicação avisos."""

from rest_framework import permissions, serializers, viewsets

from core.pagination import CorePaginator

from . import models


class AvisoSerializer(serializers.ModelSerializer):
    """Serializador de avisos."""

    class Meta:
        """Meta opções do serializador."""

        model = models.Aviso
        fields = '__all__'


class AvisoViewSet(viewsets.ModelViewSet):
    """Conjunto de views para avisos."""

    serializer_class = AvisoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = CorePaginator
    queryset = models.Aviso.objects.all()
    search_fields = ['codigo', 'descricao']
