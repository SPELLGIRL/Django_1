from django.shortcuts import render
from django.http import HttpRequest
import json

# Create your views here.


with open('static/data/main_menu_links.json', 'r', encoding='utf-8') as mml:
    main_menu_links = json.load(mml)

with open('static/data/catalog_menu_links.json', 'r', encoding='utf-8') as cml:
    catalog_menu_links = json.load(cml)

with open('static/data/trending_products.json', 'r', encoding='utf-8') as tp:
    trending_products = json.load(tp)

with open('static/data/new_products.json', 'r', encoding='utf-8') as np:
    new_products = json.load(np)

with open('static/data/exclusive_products.json', 'r', encoding='utf-8') as ep:
    exclusive_products = json.load(ep)

content = {
    'main_menu_links': main_menu_links,
    'products_menu_category': catalog_menu_links,
    'trending_products': trending_products,
    'new_products': new_products,
    'exclusive_products': exclusive_products
}


def index(request: HttpRequest):
    content['title'] = 'главная'
    return render(request, 'mainapp/index.html', content)


def products(request: HttpRequest, current_product_category='all'):
    content['title'] = 'каталог товаров'
    content['current_product_category'] = current_product_category
    return render(request, 'mainapp/products.html', content)


def details(request: HttpRequest, color='red'):
    content['current_product_category'] = ''
    content['title'] = 'товар'
    content['color'] = color
    return render(request, 'mainapp/details.html', content)


def history(request: HttpRequest):
    content['title'] = 'временная страница'
    return render(request, 'mainapp/history.html', content)


def showroom(request: HttpRequest):
    content['title'] = 'временная страница'
    return render(request, 'mainapp/showroom.html', content)


def contacts(request: HttpRequest):
    content['title'] = 'контакты'
    return render(request, 'mainapp/contacts.html', content)
