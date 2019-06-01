"""Rotas da API."""

from rest_framework import routers

from abelhas.api import AbelhaViewSet
from core.api import UserViewSet

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet)
router.register('abelhas', AbelhaViewSet)

urls = router.urls, 'bee', 'v1'
