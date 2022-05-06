
from itertools import product

from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.


def index(request):
    #  products = Products.objects.all()
    #  print(products)
    #  catProds=Products.objects.all()
    #  category=catProds.product_cat('tshirt')
    #  print(category)
    Tcate=Products.objects.filter(product_cat='tshirt')
    Wcat=Products.objects.filter(product_cat='electronics')
    params={'t_cat':Tcate , 'w_cat':Wcat}
    return render(request, 'eshop/index.html' ,params)


def tshirt(request):
  
    return render(request, 'eshop/tshirtss.html')


def contact(request):
    return render(request, 'eshop/contact.html')


def about(request):
    return render(request, 'eshop/about.html')


def productview(request):
    return HttpResponse('Creating it just wait for a while')


def exp(request):
    return render(request, 'eshop/sidebar.html')
