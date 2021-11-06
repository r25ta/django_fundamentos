from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    
    html = "<html><head><h1>Contas</h1></head><body>%s</body></html>" %(now)
    return HttpResponse(html)