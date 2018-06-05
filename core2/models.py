from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()

def _str_(self):
    return self.titulo


# Create your models here.
