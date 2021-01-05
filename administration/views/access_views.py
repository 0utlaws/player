from administration.views.actor_views import FilteredListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from administration import filters
from movies import models


class AccessListView(FilteredListView):
    model = models.Access
    template_name = 'administration/access_list.html'
    filterset_class = filters.AccessFilter
    paginate_by = 1


class AccessCreateView(SuccessMessageMixin, CreateView):
    model = models.Access
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:access-list')
    success_message = "Access successfully added!"

    fields = [
        'movie',
        'user',
        'has_access'
    ]


class AccessUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Access
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:access-list')
    success_message = "Access successfully updated!"

    fields = '__all__'

    action = 'Update'


class AccessDeleteView(SuccessMessageMixin, DeleteView):
    model = models.Access
    template_name = 'administration/form_delete.html'
    success_url = reverse_lazy('administration:access-list')
    success_message = "Access successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AccessDeleteView, self).delete(request, *args, **kwargs)