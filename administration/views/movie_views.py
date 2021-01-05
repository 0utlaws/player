from administration.views.actor_views import FilteredListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from administration import filters
from movies import models


class MovieListView(FilteredListView):
    model = models.Movie
    template_name = 'administration/movie_list.html'
    filterset_class = filters.MovieFilter
    paginate_by = 1


class MovieCreateView(SuccessMessageMixin, CreateView):
    model = models.Movie
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:movie-list')
    success_message = "Movie successfully created!"

    fields = [
        'file',
        'title',
        'description',
        'category',
        'actors'
    ]


class MovieUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Movie
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:movie-list')
    success_message = "Movie successfully updated!"

    fields = [
        'file',
        'title',
        'description',
        'category',
        'actors'
    ]

    action = 'Update'


class MovieDeleteView(SuccessMessageMixin, DeleteView):
    model = models.Movie
    template_name = 'administration/form_delete.html'
    success_url = reverse_lazy('administration:movie-list')
    success_message = "Movie successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MovieDeleteView, self).delete(request, *args, **kwargs)