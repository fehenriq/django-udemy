from django.db import models

class Produto(models.Model):
  nome = models.CharField("Nome", max_length=50)
  preco = models.DecimalField("Preço", decimal_places=2, max_digits=8)
  estoque = models.IntegerField("Quantidade em Estoque")
  
class Cliente(models.Model):
  nome = models.CharField("Nome", max_length=50)
  nome = models.CharField("Sobrenome", max_length=50)