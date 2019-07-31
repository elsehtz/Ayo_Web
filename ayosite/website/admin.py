from django.contrib import admin

# Register your models here.
from .models import order, order_item, shop_item


admin.site.register(shop_item)
admin.site.register(order)
admin.site.register(order_item)