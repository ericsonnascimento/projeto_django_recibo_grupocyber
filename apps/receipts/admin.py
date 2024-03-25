from django.contrib import admin
from . import models

class ListingReceipts(admin.ModelAdmin):
    list_display = ('id', 'client', 'user', 'date_register',)
    list_display_links = ('id', 'client',)
    search_fields = ('id', 'client',)
    list_filter = ('id', 'user', 'client',)
    #list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(models.Receipts, ListingReceipts)