# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Slike(models.Model):
    slika = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

   