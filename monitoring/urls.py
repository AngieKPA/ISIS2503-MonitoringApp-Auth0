from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include('inventory.urls')),
    path('', include('social_django.urls')),  # para Auth0
]
