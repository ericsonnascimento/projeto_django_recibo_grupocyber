from django.shortcuts import render, redirect
from . import forms


def receipts(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = forms.ReceiptsForms
    if request.method == 'POST':
        form = forms.ReceiptsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'receipts/receipts.html', {'form': form})

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'receipts/index.html')