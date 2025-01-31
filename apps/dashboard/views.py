from django.shortcuts import render
import pandas as pd
import plotly.express as px
import plotly.io as pio
from apps.receipts import models

# Create your views here.


def dashboard(request):
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

    # Criar gráfico interativo 01 usando Plotly
    fig1 = px.bar(summary_df, x='Cliente', y='Total Gasto', title='Exemplo Gasto por Cliente')
    graph_div1 = pio.to_html(fig1, full_html=False, config={'displayModeBar': False})

    # Criar gráfico interativo 02 usando Plotly
    fig2 = px.bar(summary_df, x='Cliente', y='Total Gasto', title='Exemplo Gasto por Recibo')
    graph_div2 = pio.to_html(fig2, full_html=False, config={'displayModeBar': False})

    # Criar gráfico interativo 03 usando Plotly
    fig3 = px.bar(summary_df, x='Cliente', y='Total Gasto', title='Exemplo Lucratividade por Recibo')
    graph_div3 = pio.to_html(fig3, full_html=False, config={'displayModeBar': False})
    
    return render(request, 'dashboard/dashboard.html', {'graph_div1': graph_div1, 'graph_div2': graph_div2, 'graph_div3': graph_div3})