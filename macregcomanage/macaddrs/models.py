from django.db import models

# Create your models here.

class MacAddr(models.Model):
    userEmail = models.TextField()
    macAddress  = models.TextField()
