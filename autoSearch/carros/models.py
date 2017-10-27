# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# Create your models here.
class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    make = models.CharField(max_length = 100)
    types = models.CharField(max_length = 100)
    year = models.CharField(max_length = 100)
    colour = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.make)
