# meuapp/models.py
from django.db import models

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome