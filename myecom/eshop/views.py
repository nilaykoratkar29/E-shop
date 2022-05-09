
from itertools import product

from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,Category

# Create your views here.


def home(request):
    return render(request, 'home.html')


def tshirt(request):
    tpage = Products.objects.filter(product_cat='tshirt')
    params = {'tpage': tpage}
    return render(request, 'eshop/tshirtss.html', params)


def contact(request):
    return render(request, 'eshop/contact.html')


def about(request):
    return render(request, 'eshop/about.html')


def productview(request):
 cattable=Category.objects.all()
 allprods=Products.objects.all()
 Tcate = Products.objects.filter(product_cat='tshirt')
 Ecat = Products.objects.filter(product_cat='electronics')
 Wcat = Products.objects.filter(product_cat='watch')
 params = {'t_cat': Tcate, 'e_cat': Ecat, 'w_cat': Wcat , 'procat':cattable ,'allpro':allprods}
 return render(request, 'eshop/index.html', params)


def exp(request):
    return render(request, 'eshop/sidebar.html')
