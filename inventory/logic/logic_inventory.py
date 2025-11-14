from ..models import StockItem

def get_stock_items():
    return StockItem.objects.all()

def create_stock_item(data):
    StockItem.objects.create(**data)
