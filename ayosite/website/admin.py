from django.contrib import admin
from .models import Category, Product, Order, OrderItem


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
# 
# admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)

# class ItemAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']

#     title = models.CharField(max_length=100)
#     price = models.FloatField()


# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']

#     title = models.ForeignKey(Item, on_delete=models.CASCADE)
    

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']

#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     order_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)