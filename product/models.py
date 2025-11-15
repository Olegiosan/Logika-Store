from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    cost = models.DecimalField(decimal_places=2, max_digits=12)
    count = models.IntegerField()

class ProductImages(models.Model):
    product = ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField()