from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    pass #........this is where I put my own fields

    def __str__(self):
        return self.username

# Create your models here.
