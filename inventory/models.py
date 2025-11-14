from django.db import models
from products.models import Product

class Location(models.Model):
    code = models.CharField(max_length=20, unique=True)
    warehouse = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    shelf = models.CharField(max_length=20)
    bin = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.warehouse}-{self.code}"

class StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    lot = models.CharField(max_length=50, blank=True, null=True)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
