from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.slug


class Product(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=False)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(limit_value=0,
                                                            message='Цена не мможет быть отрицательная!')])
    amount = models.IntegerField()
    img = models.ImageField(upload_to='img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug