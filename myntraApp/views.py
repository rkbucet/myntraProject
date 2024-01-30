from django.shortcuts import render
from .models import *


def homePage(self):
    products = Product.objects.all()
    context = {'products': products}
    return render(self, 'index.html', context)


def bagPage(self):
    return render(self, 'bag.html')