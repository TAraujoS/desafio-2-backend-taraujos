from django.db import models


class Documentation(models.Model):
    type = models.CharField(max_length=30)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=15)
    store_name = models.CharField(max_length=20)
