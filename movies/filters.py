import django_filters
from . import models


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')
    description = django_filters.CharFilter(field_name="description", lookup_expr='icontains')

    class Meta:
        model = models.Movie
        fields = ['title', 'description']
