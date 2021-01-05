from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from administration import forms
from movies import models


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ActorListView(TemplateView):
    template_name = 'administration/actor_list.html'


class ActorData(BaseDatatableView):
    model = models.Actor
    columns = ['name', 'surname', 'birth_place', 'picture', '']
    order_columns = ['name', 'surname', 'birth_place', '', '']

    def render_column(self, row, column):
        if column == 'birth_place':
            return mark_safe(f'<img src="{row.birth_place.flag}">')
        elif column == 'picture':
            return mark_safe(f'{row.show_pictures}')
        elif column == '':
            return mark_safe(f'''
                    <a data-pk="{row.pk}" class="btn btn-info">Edit</a>
                    <a data-pk="{row.pk}" class="btn btn-danger">Delete</a>
            ''')
        else:
            return super(ActorData, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.POST.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(name__istartswith=search) | Q(surname__istartswith=search) | Q(birth_place__istartswith=search) | Q(birth_place__istartswith=search))
        return qs


class ActorCreateView(SuccessMessageMixin, CreateView):
    model = models.Actor
    template_name = 'administration/form.html'
    form_class = forms.ActorForm
    success_url = reverse_lazy('administration:actor-list')
    success_message = "Actor successfully created!"

    def form_valid(self, form):
        actor = models.Actor.objects.create(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            birth_place=form.cleaned_data['birth_place']
        )
        for file in self.request.FILES.getlist('pictures'):
            picture = models.Picture.objects.create(image=file, actor=actor)
            picture.save()
        return redirect('administration:actor-list')


class ActorUpdateView(SuccessMessageMixin, UpdateView):
    model = models.Actor
    template_name = 'administration/form.html'
    form_class = forms.ActorForm
    success_url = reverse_lazy('administration:actor-list')
    success_message = "Actor successfully updated!"

    action = 'Update'

    def form_valid(self, form, *args, **kwargs):
        actor = models.Actor.objects.get(pk=self.kwargs['pk'])
        models.Picture.objects.filter(actor=actor).delete()
        for file in self.request.FILES.getlist('pictures'):
            picture = models.Picture.objects.create(image=file, actor=actor)
            picture.save()
        return super(ActorUpdateView, self).form_valid(form)


class ActorDeleteView(SuccessMessageMixin, DeleteView):
    model = models.Actor
    template_name = 'administration/form_delete.html'
    success_url = reverse_lazy('administration:actor-list')
    success_message = "Actor successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ActorDeleteView, self).delete(request, *args, **kwargs)