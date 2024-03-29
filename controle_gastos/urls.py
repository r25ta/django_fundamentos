"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contas.views import current_datetime, drag_race, home, nova_transacao, templatetest, listagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/',current_datetime),   
    path('drag/',drag_race),
    path("home/",home),
    path("templatetest/", templatetest),
    #mapeamento da url que o usuario irá digitar e para qual metodo da view será direcionada a request
    path("",listagem,name="url-listagem"),
    path("add-transacao/",nova_transacao,name="url-add-transacao")
]
