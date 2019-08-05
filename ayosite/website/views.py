from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from .models import Category, Product, Order, OrderItem
from django.utils import timezone


# Create your views here.
def home(request):

    #return render(request, 'web_practice_1.html', dynamic_dict)
    return render(request, 'home.html')


def shop(request, category_slug=None, slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }    
    return render(request, 'shop.html', context)
    

def room(request):
    return render(request, 'room.html', {'product_list':range(0,5)})

def order_sum(request):
    user_order = OrderItem.objects.filter(user=request.user)
    if not user_order:
        user_order = f'You have no items in your cart'
        
    return render(request, "order-summary.html", {'order_items':user_order})

def checkout(request):
    return render(request, "checkout-page.html")


def signin(request):
    return

def contact(request):

    return render(request, 'home.html')


def product_list(request, category_slug=None, slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'product/list.html', context)

def product_detail(request, slug=None):
    if slug:
        product = get_object_or_404(Product, slug=slug, available=True)
        context = {
            'product': product
        }
    else:
        context = {'product': 'Error, empty'}
    return render(request, 'product/detail.html', context)


def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, _created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False)
    order_set = Order.objects.filter(user=request.user, ordered=False)
    
    if order_set.exists():
        order = order_set[0]
        #check if order item is in the order
        if order.item.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request, "Item amount was updated in cart")
        else:
            messages.info(request, "Item added to cart")
            order.item.add(order_item)
    else:
        ordered_date =  timezone.now()
        order = Order.objects.create(user=request.user, order_date = ordered_date)
        order.item.add(order_item)   
        messages.info(request, "Item added to cart")

    return  redirect("website:product_detail", slug=slug)

def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_set = Order.objects.filter(user=request.user, ordered=False)
    
    if order_set.exists():
        order = order_set[0]
        #check if order item is in the order
        if order.item.filter(item__slug=item.slug).exists():
            order_item  = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.item.remove(order_item)
            messages.info(request, "Item removed from cart")
    else:
        #user has no extra order
        pass
    return  redirect("website:product_detail", slug=slug)