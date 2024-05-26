from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('main/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('main/create/', ProductCreateView.as_view(), name='product_create'),
    path('main/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('main/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]
