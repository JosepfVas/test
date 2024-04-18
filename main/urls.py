from django.urls import path

from main import views


urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('main/<int:pk>/', views.product_disc, name='product_disc')

]
