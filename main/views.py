from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from pytils.translit import slugify

from main.models import Product


class ProductListView(ListView):
    model = Product

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(published=True)
    #     return queryset

    def get_queryset(self):
        queryset = super().get_queryset()
        available = self.request.GET.get('published')
        if available == 'instock':
            queryset = queryset.filter(published=True)
        elif available == 'outofstock':
            queryset = queryset.filter(published=False)
        return queryset


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price', 'published')
    success_url = reverse_lazy('main:products_list')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price', 'published')
    success_url = reverse_lazy('main:product_detail')

    def get_success_url(self):
        return reverse('main:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:products_list')
