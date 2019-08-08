from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('merch', views.shop, name = 'merchandise'),
    path('merch/<slug>', views.shop, name = 'merchandise_by_category'),
    path('room', views.room, name = "room"),
    path('contact_info', views.contact, name = 'shop'),
    path('checkout-mailing', views.CheckoutView.as_view(), name = "checkout-mailing"),
    path('checkout-payment/<payment_option>', views.PaymentView.as_view(), name = "checkout-payment"),
    path('Order_Summary', views.order_sum, name = "order_summary"),
    path('product_detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('product_list', views.product_list, name='product_list'),
    path('product_list/<slug:slug>', views.product_list, name='product_list_by_category'),
    path('add_to_cart/<slug:slug>', views.add_to_cart, name = 'add_to_cart'),
    path('remove_from_cart/<slug:slug>', views.remove_from_cart, name = 'remove_from_cart') ]
