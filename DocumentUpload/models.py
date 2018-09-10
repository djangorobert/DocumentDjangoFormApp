# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    file_name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __unicdoe__(self):
        return self.name