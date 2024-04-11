from django.core.management.base import BaseCommand
from main.models import Product, Category
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('categories.json', 'r') as f:
            categories_data = json.load(f)
        return categories_data

    @staticmethod
    def json_read_products():
        with open('products.json', 'r') as f:
            products_data = json.load(f)
        return products_data

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_dict = {}
        for category in Command.json_read_categories():
            category_obj = Category.objects.create(
                name=category['fields']['name'],
                description=category['fields']['description']
            )
            category_dict[category['pk']] = category_obj

        product_for_create = []
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    name=product['fields']['name'],
                    price=product['fields']['price'],
                    description=product['fields']['description'],
                    category=category_dict.get(product['fields']['category'])
                )
            )

        Product.objects.bulk_create(product_for_create)
