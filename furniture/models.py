from django.core.validators import MinValueValidator
from django.db import models


class Furniture(models.Model):
    provider = models.ForeignKey(
        "Provider", on_delete=models.CASCADE, related_name="furniture"
    )
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="furniture/")

    class Meta:
        db_table = "furniture"
        verbose_name = "Furniture"
        verbose_name_plural = "Furniture"

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
