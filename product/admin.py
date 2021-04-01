from django.contrib import admin
from product.models import Product, Cart, ItemQuantity

admin.site.register(Product)
admin.site.register(ItemQuantity)
admin.site.register(Cart)
