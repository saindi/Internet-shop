from django.db import models


class User(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)