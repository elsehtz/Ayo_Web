from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Category, Product, Order, OrderItem
from django.utils import timezone


# Create your views here.
def home(request):

    #return render(request, 'web_practice_1.html', dynamic_dict)
    return render(request, 'web_practice_1.html')


def shop(request):
    return render(request, 'shop.html')
    

def room(request):
    return render(request, 'room.html', {'product_list':range(0,5)})


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

# def product_detail(request, id, slug):
def product_detail(request, slug=None):
    # product = get_object_or_404(Product, id=id, slug=slug, available=True)
    if slug:
        product = get_object_or_404(Product, slug=slug, available=True)
        context = {
            'product': product
        }
    else:
        context = {'product': 'Error, empty'}
    return render(request, 'product/detail.html', context)


def checkout(request):
    return render(request, "checkout-page.html")

def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_set = Order.objects.filter(user=request.user, ordered=False)
    
    if order_set.exists():
        order = order_set[0]
        #check if order item is in the order
        if order.item.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
    else:
        ordered_date =  timezone.now()
        order = Order.objects.create(user=request.user, order_date = ordered_date)
        order.items.add(order_item)   

    return  redirect("website:product_detail", slug=slug)