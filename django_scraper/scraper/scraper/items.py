from scrapy_djangoitem import DjangoItem
from product.models import data

class ProductItem(DjangoItem):
    django_model = data
