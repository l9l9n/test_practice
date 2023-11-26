from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    mode = models.CharField(verbose_name='Режим')
    mode1 = models.CharField(verbose_name='Режим')
    # change mode
