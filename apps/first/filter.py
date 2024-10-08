from django_filters import rest_framework as filters

from apps.first.choices.boody_type_choices import BodyTypeChoices


class CarFilter(filters.FilterSet):
    year_gtd = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year_range = filters.RangeFilter('year')
    year_in = filters.BaseInFilter('year')
    body = filters.ChoiceFilter('body', choices=BodyTypeChoices.choices)
    order = filters.OrderingFilter(fields=('brand', 'price'))
