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
    if not request.user.is_authenticated:
        return redirect('login')

    form = forms.UserRegistrationForm()

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)

        if form.is_valid():
            name_registration = form['name_registration'].value()
            login_registration = form['login_registration'].value()
            password_registration = form['password'].value()

        if User.objects.filter(username=name_registration).exists():
            return redirect('cadastro_acesso')

        user = User.objects.create_user(
            username=login_registration,
            first_name=name_registration,
            password=password_registration
        )
        user.save()
        return redirect('index')

    return render(request, 'users/cadastro_acesso.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')