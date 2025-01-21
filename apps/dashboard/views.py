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

    # Criar gráfico interativo usando Plotly
    fig = px.bar(summary_df, x='Cliente', y='Total Gasto', title='Total Gasto por Cliente')
    graph_div = pio.to_html(fig, full_html=False)

    return render(request, 'dashboard/dashboard.html', {'graph_div': graph_div})