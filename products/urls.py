from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('products/create/', views.product_create, name='product_create'),
]
