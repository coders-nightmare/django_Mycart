from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.


def index(request):
    products = Product.objects.all()
    print(products)
    # n = len(products)
    # nSlides = n//3+ceil((n/3)-(n//3))
    # 1)
    # params = {'product': products,
    #           'no_of_slides': nSlides, 'range': range(nSlides)}
    # 2)
    # allprods=[[products,range(1,nSlides),nSlides],
    #           [products, range(1, nSlides), nSlides]]
    allprods = []
    # it return all queryset value category in form of list of dictionaries
    catProds = Product.objects.values('category')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//3+ceil((n/3)-(n//3))
        allprods.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allprods}

    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("we are at contact")


def tracker(request):
    return HttpResponse("we are at tracker")


def search(request):
    return HttpResponse("we are at search")


def productview(request):
    return HttpResponse("we are at productview")


def checkout(request):
    return HttpResponse("we are at checkout")
