from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('merch', views.shop, name = 'merchandise'),
    path('room', views.room, name = "room"),
    path('contact_info', views.contact, name = 'shop'),
    path('add', views.add, name = 'add'),
    path('product_detail', views.product_detail, name='product_detail'),
    path('product_list', views.product_list, name='product_list'), ]
