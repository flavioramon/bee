"""Rotas da API."""

from rest_framework import routers

from abelhas.api import AbelhaViewSet, EspecieAbelhaViewSet, PaisAbelhaViewSet, TipoAbelhaViewSet
from avisos.api import AvisoViewSet
from core.api import UserViewSet

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet)

router.register('abelhas', AbelhaViewSet)
router.register('abelhas-especie', EspecieAbelhaViewSet)
router.register('abelhas-tipo', TipoAbelhaViewSet)
router.register('abelhas-pais', PaisAbelhaViewSet)

router.register('avisos', AvisoViewSet)

urls = router.urls, 'bee', 'v1'
