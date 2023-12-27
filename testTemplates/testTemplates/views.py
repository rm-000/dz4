from django.shortcuts import render

menu = {'главная':'/', 'о блоге':'/about', 'комментарии':'/comments'}

def about_page(request):
    title = 'О блоге'
    data = {'menu':menu, 'title':title}
    return render(request, "./about.html", context = data)

def article1(request):
    title = 'Статья 1'
    data = {'menu':menu, 'title':title}
    return render(request, "./article1.html", context = data)

def article2(request):
    title = 'Статья 2'
    data = {'menu':menu, 'title':title}
    return render(request, "./article2.html", context = data)

def article3(request):
    title = 'Статья 3'
    data = {'menu':menu, 'title':title}
    return render(request, "./article3.html", context = data)