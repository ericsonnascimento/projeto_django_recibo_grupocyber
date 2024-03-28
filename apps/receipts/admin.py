from django.contrib import admin
from . import models

class ListingReceipts(admin.ModelAdmin):
    empty_value_display = "vazio" #substitui valores vazios pela string digitada
    list_display = ('id', 'client', 'user', 'date_register',)
    list_display_links = ('id', 'client',)
    search_fields = ('id', 'client',)
    list_filter = ('id', 'user', 'client',)
    #list_editable = ('publicada',)
    #fields = ('price',) #na tela de edição, serão mostrados apenas os campos listados aqui
    #exclude = ('price',) #na tela de edição, será excluido o campo desta lista
    list_per_page = 10

admin.site.register(models.Receipts, ListingReceipts)

#