from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models
import pandas as pd
import plotly.express as px
import plotly.io as pio


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

def receipts_edit(request, id_receipt):
    if not request.user.is_authenticated:
        return redirect('login')

    receipt_instance = models.Receipts.objects.get(id=id_receipt)
    form = forms.ReceiptsRegisterForms(instance=receipt_instance)

    if request.method == 'POST':
        form = forms.ReceiptsRegisterForms(request.POST, instance=receipt_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recibo alterado com sucesso!')
            return redirect('receipts_list')

    return render(request, 'receipts/receipts_edit.html', {'form':form, 'id_receipt':id_receipt})

def receipts_delete(request, id_receipt):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        receipt_instance = models.Receipts.objects.get(id=id_receipt)
        receipt_instance.delete()
        messages.success(request, 'Recibo excluído com sucesso!')
        return redirect('receipts_list')

    return render(request, 'receipts/receipts_delete.html', {'id_receipt':id_receipt})

def index(request):
    # Extrair dados dos recibos e clientes
    receipts = models.Receipts.objects.all()
    clients = models.Client_Register.objects.all()

    # Convertendo dados para DataFrame para facilitar a manipulação com Pandas
    receipts_df = pd.DataFrame(list(receipts.values('client__name', 'price', 'date_register')))

    # Limpar e converter os dados conforme necessário
    receipts_df['price'] = receipts_df['price'].str.replace('R$', '').str.replace(',', '.').astype(float)

    # Agrupar por cliente e somar os preços
    summary_df = receipts_df.groupby('client__name').agg({'price': 'sum'}).reset_index()
    summary_df.columns = ['Cliente', 'Total Gasto']

    # Criar gráfico interativo usando Plotly
    fig = px.bar(summary_df, x='Cliente', y='Total Gasto', title='Total Gasto por Cliente')
    graph_div = pio.to_html(fig, full_html=False)

    return render(request, 'receipts/index.html', {'graph_div': graph_div})

