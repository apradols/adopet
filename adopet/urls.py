from django.contrib import admin
from django.urls import path
from adopet.views import index, home, login, cadastro, mensagem, perfil

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('mensagem/', mensagem, name='mensagem'),
    path('perfil/', perfil, name='perfil'),
]
