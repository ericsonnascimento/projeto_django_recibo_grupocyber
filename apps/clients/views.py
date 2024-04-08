from django.shortcuts import render, redirect
from django.contrib import messages
from . import models
from . import forms

def client_register(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = forms.ClientRegisterForms
    if request.method == 'POST':
        form = forms.ClientRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('index')

    return render(request, 'clients/client_register.html', {'form': form})

def client_list(request):
    clients = models.Client_Register.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})
