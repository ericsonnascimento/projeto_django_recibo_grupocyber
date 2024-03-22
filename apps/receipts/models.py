from django.db import models
from django.contrib.auth.models import User
from apps.clients.models import Client_Register

class Receipts(models.Model):
    date_register = models.DateTimeField(auto_now_add=True, blank=False)
    price = models.CharField(max_length=10, null=False, blank=False)
    text = models.TextField(max_length=500, null=False, blank=False)
    client = models.ForeignKey(
        to=Client_Register,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='name_fk',
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user_fk',
    )

    def __str__(self):
        return self.text





