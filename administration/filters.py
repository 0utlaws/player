import django_filters
from movies import models


class ActorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    surname = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Actor
        fields = ['name', 'surname', 'birth_place']


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Category
        fields = ['name', 'description']


class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Movie
        fields = ['title', 'description', 'category', 'actors']


class AccessFilter(django_filters.FilterSet):
    class Meta:
        model = models.Access
        fields = '__all__'
