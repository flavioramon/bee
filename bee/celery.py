"""Módulo de configuração celery."""

import os

import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bee.settings')

app = celery.Celery('bee')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
