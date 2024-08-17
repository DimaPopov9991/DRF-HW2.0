from django.db import models

from apps.auto_parks.models import AutoParkModel
from apps.first.choices.boody_type_choices import BodyTypeChoices
from apps.first.managers import CarManager
from core.models import BaseModel
from django.core import validators as V
from datetime import datetime

# Create your models here.
class Car(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)
    brand=models.CharField(max_length=10, validators=(V.MinLengthValidator(2),))
    price=models.IntegerField(validators=(V.MinValueValidator(0), V.MaxValueValidator(1000000)))
    year=models.IntegerField(validators=(V.MinValueValidator(1990), V.MaxValueValidator(datetime.now().year)))
    body_type=models.CharField(max_length=9, choices=BodyTypeChoices.choices)
    auto_park=models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    objects=CarManager()
    


