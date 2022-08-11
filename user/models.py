from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    img = models.ImageField(upload_to='user/img', default='user/img/user_img.png')
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username}, {self.first_name}, {self.last_name}"

    class Meta:
        verbose_name = "користувач"
        verbose_name_plural = "користувачі"
