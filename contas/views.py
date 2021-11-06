from django.shortcuts import render
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html="<html><head><h1>Contas</h1></head><body>horário %s</body></html>" %(now)
    return HttpResponse(html)

def numeros_pares(request):
    table=""
    cont_col=1
    table_row=""
    
    for i in range (1000):
        if (i%2==0):
            table_row +="<td>%d</td>" %(i)
            cont_col +=1
        
        #QUEBRA POR COLUNAS        
        if cont_col == 20:
            cont_col = 1
            table += "<tr>" + table_row + "</tr>"
            table_row=""               
        
    
    x = "<table>"+table+"</table>"
            
    html= "<html><head><h1>Números Pares</head><body>%s</body></html>" %(x)    
    return HttpResponse(html)    
    