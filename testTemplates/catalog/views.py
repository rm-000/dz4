from django.shortcuts import render
from .models import Product

menu = {'главная':'/', 'о блоге':'/about'}

def main_page(request):
    products = Product.objects.all()
    title = 'Блог'
    data = {'menu':menu, 'title':title, 'products':products}
    return render(request, "./index.html", context = data)

def add_comment_page(request):
    title = 'Добавить комментарий'
    data = {'menu':menu, 'title':title}
    return render(request, "./add_comment.html", context = data)

def thanks_page(request):
    user_name = request.POST['user_name']
    title = 'Страница благодарности'
    data = {'menu':menu, 'title':title, 'user_name':user_name}
    return render(request, "./thanks.html", context = data)