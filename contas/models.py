from django.db import models
from django.db.models.fields import CharField, DateTimeField

# Create your models here.
class Categoria(models.Model):
    nome = CharField(max_length=100)
    dt_criacao = DateTimeField(auto_now_add=True)       