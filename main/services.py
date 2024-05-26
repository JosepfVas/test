from django.core.cache import cache

from config.settings import CACHE_ENABLED
from main.models import Product


def get_products_from_cache():
    """Получаем список продуктов из кэша, если кэш пуст-получаем из БД."""
    if CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
