from django.shortcuts import render

# Create your views here.

links_menu = [
    {'href': 'home', 'name': 'HOME'},
    {'href': 'catalog', 'name': 'PRODUCTS'},
    {'href': 'history', 'name': 'HISTORY'},
    {'href': 'showroom', 'name': 'SHOWROOM'},
    {'href': 'contacts', 'name': 'CONTACT'}
]
content = {
    'title': '',
    'links_menu': links_menu
}

def index(request):
    content['title'] = 'главная'
    return render(request, 'mainapp/index.html', content)


def products(request):
    content['title'] = 'каталог товаров'
    return render(request, 'mainapp/products.html', content)


def details(request):
    content['title'] = 'товар'
    return render(request, 'mainapp/details.html', content)


def history(request):
    content['title'] = 'временная страница'
    return render(request, 'mainapp/history.html', content)


def showroom(request):
    content['title'] = 'временная страница'
    return render(request, 'mainapp/showroom.html', content)


def contacts(request):
    content['title'] = 'контакты'
    return render(request, 'mainapp/contacts.html', content)
