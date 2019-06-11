"""Rotas da API."""

from rest_framework import routers

from core.api import UserViewSet
from leituras.api import LeituraViewSet

router = routers.DefaultRouter()
router.register('usuarios', UserViewSet)
router.register('leituras', LeituraViewSet)

urls = router.urls, 'bee', 'v1'
