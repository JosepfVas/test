from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from pytils.translit import slugify

from version.forms import VersionForm
from version.models import Version


class VersionListView(ListView):
    model = Version

    def get_queryset(self):
        queryset = super().get_queryset()
        available = self.request.GET.get('published')
        if available == 'instock':
            queryset = queryset.filter(published=True)
        elif available == 'outofstock':
            queryset = queryset.filter(published=False)
        return queryset


class VersionDetailView(DetailView):
    model = Version

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('version:version_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.slug = slugify(new_blog.title)
            if len(form.cleaned_data['description']) == 0:
                new_blog.published = False
            else:
                new_blog.published = True
            new_blog.save()
        return super().form_valid(form)


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm

    def get_success_url(self):
        return reverse('version:version_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.description)
            new_blog.save()

        return super().form_valid(form)


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('version:version_list')
