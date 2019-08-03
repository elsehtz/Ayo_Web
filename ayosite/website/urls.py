from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('merch', views.shop, name = 'merchandise'),
    path('room', views.room, name = "room"),
    path('contact_info', views.contact, name = 'shop'),
    path('checkout', views.checkout, name = "checkout"),
    path('product_detail', views.product_detail, name='product_detail'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),
    path('product_list', views.product_list, name='product_list'),
    path('product_list/<slug:slug>', views.product_list, name='product_list_by_category'), ]
