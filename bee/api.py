"""Rotas da API."""

from rest_framework import routers

from abelhas.api import AbelhaViewSet, EspecieAbelhaViewSet, PaisAbelhaViewSet, TipoAbelhaViewSet
from core.api import UserViewSet

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet)
router.register('abelhas', AbelhaViewSet)
router.register('abelhas-especie', EspecieAbelhaViewSet)
router.register('abelhas-tipo', TipoAbelhaViewSet)
router.register('abelhas-pais', PaisAbelhaViewSet)

urls = router.urls, 'bee', 'v1'
