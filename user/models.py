from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Покупець"
        verbose_name_plural = "Покупці"