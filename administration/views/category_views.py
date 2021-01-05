from django.contrib import messages

from administration.views.actor_views import FilteredListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from administration import filters
from movies import models


class CategoryListView(FilteredListView):
    model = models.Category
    template_name = 'administration/category_list.html'
    filterset_class = filters.CategoryFilter
    paginate_by = 1


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = models.Category
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:category-list')
    success_message = "Category successfully created!"

    fields = [
        'name',
        'description'
    ]


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Category
    template_name = 'administration/form.html'
    success_url = reverse_lazy('administration:category-list')
    success_message = "Category successfully updated!"

    fields = [
        'name',
        'description'
    ]

    action = 'Update'


class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    model = models.Category
    template_name = 'administration/form_delete.html'
    success_url = reverse_lazy('administration:category-list')
    success_message = "Category successfully created!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CategoryDeleteView, self).delete(request, *args, **kwargs)