from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.clients.urls')),
    path('', include('apps.receipts.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.dashboard.urls')),
]
