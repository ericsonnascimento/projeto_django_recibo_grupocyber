from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
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
            return redirect('dashboard')

    return render(request, 'clients/client_register.html', {'form': form})

def client_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    clients_instance = models.Client_Register.objects.all()
    return render(request, 'clients/client_list.html', {'clients_instance': clients_instance})

def client_edit(request, id_client):
    if not request.user.is_authenticated:
        return redirect('login')
    
    client_instance = models.Client_Register.objects.get(id=id_client)
    form = forms.ClientRegisterForms(instance=client_instance)

    if request.method == 'POST':
        form = forms.ClientRegisterForms(request.POST, instance=client_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente alterado com sucesso!')
            return redirect('client_list')
        
    return render(request, 'clients/client_edit.html', {'form': form, 'id_client': id_client})

def client_delete(request, id_client):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        client_instance = models.Client_Register.objects.get(id=id_client)
        client_instance.delete()
        messages.success(request, 'Cliente excluido com sucesso!')
        return redirect('client_list')
    
    return render(request, 'clients/client_delete.html', {'id_client': id_client})

def client_search(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    query = request.GET.get('search')

    if query:
        client_instance = models.Client_Register.objects.filter(
            Q(id__icontains=query) |
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
            ).order_by('id')
    else:
        client_instance = models.Client_Register.objects.all().order_by('id')

    return render(request, 'clients/client_list.html', {'clients_instance':client_instance})