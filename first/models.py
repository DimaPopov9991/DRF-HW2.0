from django.db import models

# Create your models here.
class Car(models.Model):
    class Meta:
        db_table = 'cars'
    brand=models.CharField(max_length=255)
    price=models.IntegerField()
    year=models.IntegerField()

