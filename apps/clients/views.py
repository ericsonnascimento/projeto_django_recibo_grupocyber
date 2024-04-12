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
    if not request.user.is_authenticated:
        return redirect('login')
    
    clients = models.Client_Register.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_edit(request, id_client):
    if not request.user.is_authenticated:
        return redirect('login')
    
    clients = models.Client_Register.objects.get(id=id_client)
    form = forms.ClientRegisterForms(instance=clients)

    if request.method == 'POST':
        form = forms.ClientRegisterForms(request.POST, instance=clients)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente alterado com sucesso!')
            return redirect('client_list')
        
    return render(request, 'clients/client_edit.html', {'form': form, 'id_client': id_client})

def client_delete(request, id_client):
    if not request.user.is_authenticated:
            return redirect('login')

    id_client = models.Client_Register.objects.get(id=id_client)
    id_client.delete()
    messages.success(request, 'Deleção realizada com sucesso!')

    return redirect('client_list')
    
