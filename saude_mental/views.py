from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após o registro
            return redirect('/')  # Redireciona para a página inicial
    else:
        form = UserRegistrationForm()
    return render(request, 'contanova.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Utilize get para evitar erros caso a chave não exista
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/static/meses/jan.html')  
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    return render(request, 'index.html')  # Renderiza o template de login

def index(request):
    return render(request, 'index.html')  # Página inicial do site
