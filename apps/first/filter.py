from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.first.models import Car


def carfilter(query:QueryDict)-> QuerySet:
    qs=Car.objects.all()



    for k,v in query.items():
        match k:
            case 'price_gt':
                qs=qs.filter(price__gt=v)
            case 'price_lt':
                qs=qs.filter(price__lt=v)
            case _:
                raise ValidationError(f"Invalid value for {k}")
    return qs



