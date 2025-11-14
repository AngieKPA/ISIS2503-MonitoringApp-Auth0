from ..models import Product

def get_products():
    return Product.objects.filter(is_active=True)

def get_product(id):
    return Product.objects.filter(id=id).first()

def create_product(data):
    Product.objects.create(**data)
