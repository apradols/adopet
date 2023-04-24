from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')

def mensagem(request):
    return render(request, 'mensagem.html')

def perfil(request):
    return render(request, 'perfil.html')