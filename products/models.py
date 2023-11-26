from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    mode12 = models.CharField(verbose_name="Help")