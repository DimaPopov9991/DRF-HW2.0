from django.db import models

from core.models import BaseModel


# Create your models here.
class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['id']
    name=models.CharField(max_length=20)
