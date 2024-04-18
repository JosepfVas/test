from django.shortcuts import render, get_object_or_404

from main.models import Category, Product


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'main/products.html', context)


def product_disc(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'main/product_disc.html', context)
