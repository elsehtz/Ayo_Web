from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('merch', views.shop, name = 'merchandise'),
    path('room', views.room, name = "room"),
    path('contact_info', views.contact, name = 'contact_info'),
    path('add', views.add, name = 'add')
]