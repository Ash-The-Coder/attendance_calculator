from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(_("username"), unique=True, max_length=150,default="")


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.username