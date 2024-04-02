from django_filters import rest_framework as filters
from .models import Vacancy


class VacancyFilter(filters.FilterSet):
    min_salary = filters.NumberFilter(field_name="job__salary", lookup_expr='gte')
    max_salary = filters.NumberFilter(field_name="job__salary", lookup_expr='lte')

    class Meta:
        model = Vacancy
        fields = ['category']

