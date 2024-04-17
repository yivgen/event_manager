from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from users.managers import CustomUserManager

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    is_admin = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email