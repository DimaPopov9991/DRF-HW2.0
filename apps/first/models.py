from django.db import models

from core.models import BaseModel


# Create your models here.
class Car(BaseModel):
    class Meta:
        db_table = 'cars'
    brand=models.CharField(max_length=255)
    price=models.IntegerField()
    year=models.IntegerField()

