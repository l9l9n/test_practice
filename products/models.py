from django.db import models


class Product(models.Model):
    name2 = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7,decimal_places=2)
