from django.db import models
from datetime import datetime


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Receita(BaseModel):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
