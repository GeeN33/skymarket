from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ADMIN = "admin"
    USER = "user"

    ROLE = [(ADMIN, "admin"), (USER, "user")]

    last_login  = models.DateTimeField(null=True)
    phone = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLE, default=USER)
    email = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["username"]



