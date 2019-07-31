from django.shortcuts import render
from django.http import HttpResponse
from .models import shop_item, names
# Create your views here.
def home(request):
    shirt_ex = shop_item()
    my_name = names()
    my_name.name = "Zak E."
    dynamic_dict = """NOTE**: THIS IS JUST SAMPLE TEXT TO SHOW THAT THIS IS A DYNAMIC 
                    TEXT SECTION FOR WHATEVER USES YOU MAY HAVE ~ Zak \n\n
                    "Whatever may come, fast or progressive, forcefully or quietly, abrasive or other. 
                    Do not waiver, do not weaken, do not fall. Failure may feel like
                    the heaviest weight, but in reality, nothing is heavier than despair" """
    
    #return render(request, 'web_practice_1.html', dynamic_dict)
    return render(request, 'web_practice_1.html', {'dest_1':my_name})


def shop(request):
    return render(request, 'checkout-page.html')


def room(request):
    return render(request, 'room.html', {'product_list':range(0,5)})


def signin(request):
    return


def contact(request):
    return render(request, 'home.html')

# Actions

def add(request):
    val_1 = request.POST['num_1']
    val_2 = request.POST['num_2']
    res = int(val_1) + int(val_2)
    return render(request, 'result.html', {'result':res})