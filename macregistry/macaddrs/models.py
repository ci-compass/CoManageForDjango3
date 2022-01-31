from django.db import models

# Create your models here.

class MacAddr(models.Model):
    username = models.TextField()
    address  = models.TextField()

    
