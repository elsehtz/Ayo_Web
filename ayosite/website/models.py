from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


#=======================================================================

class shop_item(models.Model):
    app_label = 'website'
    title = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 100)
    #price = models.FloatField()
    class Meta:
        app_label = 'website'
    def __str__(self):
        return self.title


class order_item(models.Model):
    item = models.ForeignKey(shop_item,on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title


class order(models.Model):
    user = models.ForeignK ey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    order = models.BooleanField(default = False)
    items = models.ManyToManyField(order_item)
    # start_date = models.DateTimeField(auto_now_add=True)
    # order_date = models.DateTimeField()
    
    # def __str__(self):
    #     return self.user.username

class CustomUser(models.Model):
    title: models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Cart(models.Model):
    # created_at = models.DateTimeField(auto_now_add = True)
    user = models.OneToOneField(CustomUser, blank=True, null=True, on_delete = models.CASCADE, related_name='cart')
    session_key = models.CharField(max_length=40)

    class Meta:
        unique_together = ('user', 'session_key',)

class names(models.Model):
    name: str