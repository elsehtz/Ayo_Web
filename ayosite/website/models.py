from django.db import models

# Create your models here.
class shop_item(models.Model):
    name: models.CharField(max_length = 100)
    desc: models.CharField(max_length = 100)
    price: models.FloatField()

class order_item(models.Model):
    pass

class order(models.Model):
    name: models.CharField(max_length = 100)

class names():
    name: str()