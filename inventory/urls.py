from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_list, name='inventory'),
    path('inventory/create/', views.inventory_create, name='inventory_create'),
]
