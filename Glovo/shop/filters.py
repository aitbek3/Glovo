from django_filters import FilterSet
from .views import *


class ProductFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            'price': ['gt', 'lt'],
            'category': ['exact'],
            'resto_name': ['exact'],
        }
