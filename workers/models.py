from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_started = models.DateField()
    category = models.CharField(max_length=200, null=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
