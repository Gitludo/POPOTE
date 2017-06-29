from __future__ import unicode_literals
from django.db import models
import sqlite3

class Stock(models.Model):
    produit = models.CharField(max_length=20)
    quantite = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):

        return self.produit
