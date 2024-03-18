from django.db import models

class Client_Register(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name