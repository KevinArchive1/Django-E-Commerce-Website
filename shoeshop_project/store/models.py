from django.db import models

# Create your models here.

class Shoes(models.Model):
    CATEGORY_CHOICE = [
        ("shoes", "Shoes"),
        ("slippers", "Slippers"),
        ("boots", "Boots"),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="shoe/", blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE, default="shoes")
    description = models.TextField(max_length=100, null=True)

    

    def __str__(self) -> str:
        return self.name