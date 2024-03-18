from django.shortcuts import render, redirect
from . import forms

def client_register(request):
    form = forms.ClientRegisterForms
    if request.method == 'POST':
        form = forms.ClientRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'clients/client_register.html', {'form': form})
