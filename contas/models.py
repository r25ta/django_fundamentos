from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField

# Create your models here.
class Categoria(models.Model):
    nome = CharField(max_length=100)
    dt_criacao = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
        
class Transacao(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=CASCADE)
    observacoes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.descricao
    
    #CRIA APELIDO PARA CLASSE
    class Meta:
        verbose_name_plural = "Trasacoes"