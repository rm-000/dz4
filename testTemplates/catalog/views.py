from django.shortcuts import render
from .models import Product

menu = {'главная':'/', 'о блоге':'/about'}

def main_page(request):
    products = Product.objects.all()
    title = 'Блог'
    data = {'menu':menu, 'title':title, 'products':products}
    return render(request, "./index.html", context = data)