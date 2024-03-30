from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms


def receipts(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = forms.ReceiptsForms
    if request.method == 'POST':
        form = forms.ReceiptsForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recibo cadastrado com sucesso!')
            return redirect('index')

    return render(request, 'receipts/receipts.html', {'form': form})

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'receipts/index.html')