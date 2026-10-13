import django_filters
from .models import Employee
class CustomFilter(django_filters.FilterSet):
    min_age=django_filters.NumberFilter(field_name='age',lookup_expr='gte')
    max_age=django_filters.NumberFilter(field_name='age',lookup_expr='lte')
    name=django_filters.CharFilter(field_name='name',lookup_expr='icontains')

    class Meta:
        model=Employee
        fields=['min_age','max_age','name']