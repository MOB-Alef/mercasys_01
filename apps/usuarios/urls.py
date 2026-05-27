"""
=====================================================
PROJETO: MercaSys
ARQUIVO: urls.py
STATUS: EM DESENVOLVIMENTO
=====================================================

OBJETIVO:
Gerenciar URLs do app de usuários.
=====================================================
"""

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]