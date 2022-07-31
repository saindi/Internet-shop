from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()


class Product(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=False)
    description = models.TextField()
    price = models.IntegerField()
    amount = models.IntegerField()
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)