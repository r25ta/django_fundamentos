from django.shortcuts import render
from django.http import HttpResponse
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