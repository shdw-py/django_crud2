# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('lista/', views.lista_produtos , name='lista_produtos'),
    path('cria/', views.cria_produto , name='cria_produto'),
    path('atualiza/<int:pk>/', views.atualiza_produto, name='atualiza_produto'),
    path('deleta/<int:pk>/', views.deleta_produto, name='deleta_produto'),
]