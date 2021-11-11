from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Transacao

class TransacaoForm(ModelForm):
    class Meta():
        model = Transacao
        fields = ['data','categoria','descricao','valor','observacoes']