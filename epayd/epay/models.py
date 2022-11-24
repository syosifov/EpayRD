from django.db import models

class Merchant(models.Model):

    min = models.CharField(max_length=40,unique=True)
    secret = models.CharField(max_length=255)


