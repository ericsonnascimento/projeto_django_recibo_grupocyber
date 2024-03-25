from django.contrib import admin
from . import models

class ListingClients(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone',)
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'client',)
    list_filter = ('id', 'name', 'phone')
    list_per_page = 10

admin.site.register(models.Client_Register, ListingClients)