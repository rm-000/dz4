from django.shortcuts import render
from .models import Product, ProductComment

menu = {'главная':'/', 'о блоге':'/about', 'комментарии':'/comments'}

def main_page(request):
    products = Product.objects.all()
    title = 'Блог'
    data = {'menu':menu, 'title':title, 'products':products}
    return render(request, "./index.html", context = data)

def thanks_page(request):
    user_name = request.POST['user_name']
    email = request.POST['email']
    feedback = request.POST['feedback']
    product = Product.objects.get(pk=request.POST['product'])
    ProductComment.objects.create(user_name=user_name, email=email, feedback=feedback, product=product)
    title = 'Страница благодарности'
    data = {'menu':menu, 'title':title, 'user_name':user_name, 'email':email, 'feedback':feedback}
    return render(request, "./thanks.html", context = data)

def comments(request):
    products = Product.objects.values('id', 'name')
    title = 'Комментарии'
    comment = ProductComment.objects.filter(checkbox=True).order_by('-id')
    data = {'menu':menu, 'title':title, 'products':products, 'comment': comment}
    return render(request, "./comments.html", context=data)