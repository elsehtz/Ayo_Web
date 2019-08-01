from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product


# Create your views here.
def home(request):

    #return render(request, 'web_practice_1.html', dynamic_dict)
    return render(request, 'web_practice_1.html')


def shop(request):
    return render(request, 'checkout-page.html')
    

def room(request):
    return render(request, 'room.html', {'product_list':range(0,5)})


def signin(request):
    return


def contact(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'home.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'shop/product/detail.html', context)
# Actions

def add(request):
    val_1 = request.POST['num_1']
    val_2 = request.POST['num_2']
    res = int(val_1) + int(val_2)
    return render(request, 'result.html', {'result':res})