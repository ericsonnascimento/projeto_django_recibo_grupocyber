from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models


def receipts_register(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = forms.ReceiptsRegisterForms
    if request.method == 'POST':
        form = forms.ReceiptsRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recibo cadastrado com sucesso!')
            return redirect('index')

    return render(request, 'receipts/receipts_register.html', {'form': form})

def receipts_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    receipts_instance = models.Receipts.objects.all()
    return render(request, 'receipts/receipts_list.html', {'receipts_instance': receipts_instance})


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'receipts/index.html')