from django.shortcuts import redirect, render
from django.http import HttpResponse
from contas.models import Transacao
from contas.form import TransacaoForm

import datetime


# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    
    html = "<html><head><h1>Contas</h1></head><body>%s</body></html>" %(now)
    return HttpResponse(html)

def drag_race(request):
    html = "<html><body><iframe width='1300' height='615' src='https://www.youtube.com/embed/tuZCd7dBx3I' title='YouTube video player' frameborder='25' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe></body></html>"
    return HttpResponse(html)

def home(request):
    return render(request,"contas/home.html")

def templatetest(request):
    dados=dict()
    now = datetime.datetime.now()
    dados["data"] = now
    
    nomes = ['Ronaldo da Conceição', 'Olivia Cardoso Cruz Conceição', 'Diego Cruz Conceição','Camila Cruz Conceição']
    
    dados["nomes"] = nomes
    
    return render(request,'contas/template_test.html',dados)    

#Listar objetos do banco de dados
def listagem(request):
    #Criar dicionario que será enviado para browser
    data = dict()
    #Consulta os registros do BD através da Model Transacao
    data["transacoes"] = Transacao.objects.all()
    
    #Retorna request, a página html e os dados extraidos da base de dados
    return render(request, 'contas/listagem.html' ,data)

def nova_transacao(request):
    data = dict()
    form = TransacaoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("url-listagem")
        
    data['form'] = form
    
    return render(request, 'contas/form_transacao.html',data)
    