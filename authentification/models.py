from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.TextChoices):
    ADMIN = "admin"
    USER = "user"

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=100, null=True)
    balance = models.DecimalField(decimal_places=2, max_digits=11, null=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER, null=True)