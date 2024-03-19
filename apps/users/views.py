from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from . import forms

def login(request):
    form = forms.LoginForms()

    if request.method == 'POST':
        form = forms.LoginForms(request.POST)

        if form.is_valid():
            login_name = form['login_name'].value()
            login_password = form['login_password'].value()

        usuario = auth.authenticate(
            username=login_name,
            password=login_password,
        )

        if usuario is not None:
            auth.login(request, usuario)
            return redirect('index')

    return render(request, 'users/login.html', {'form': form})

def cadastro_acesso(request):
    return render(request, 'users/cadastro_acesso.html')

def logout(request):
    return render(request, 'users/logout.html')