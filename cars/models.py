from django.db import models
from buyers.models import Buyer
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self) -> str:
        return f"{self.name}-{self.price}-{self.buyer}"        