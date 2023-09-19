from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos , name='lista_produtos'),
    path('cria/', views.cria_produto , name='cria_produto'),
    path('atualiza/<int:pk>/', views.atualiza_produto, name='atualiza_produto'),
    path('deleta/<int:pk>/', views.deleta_produto, name='deleta_produto'),
]