from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    available = models.BooleanField(default=False)
    description = models.TextField(max_length=100)
    price = models.IntegerField()