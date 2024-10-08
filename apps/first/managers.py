from django.db import models


class CarQuerySet(models.QuerySet):
    def les_than_year(self, year):
        return self.filter(year__lt=year)
    def only_audi(self):
        return self.filter(brand='Audi')

class CarManager(models.Manager):

    def get_queryset(self):
        return CarQuerySet(self.model)
    def les_than_year(self, year):
        return self.get_queryset().les_than_year(year)

    def only_audi(self):
        return self.get_queryset().only_audi()