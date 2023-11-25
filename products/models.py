from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    mode = models.CharField(verbose_name='Режим')
    mode2 = models.CharField(verbose_name='Режим')
    mode3 = models.CharField(verbose_name='Режим')
    mode4 = models.CharField(verbose_name='Режим')
    mode5 = models.CharField(verbose_name='Режим')
    mode6 = models.CharField(verbose_name='Режим')
    # change mode
