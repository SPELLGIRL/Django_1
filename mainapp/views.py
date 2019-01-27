from django.shortcuts import render
from django.http import HttpRequest
from random import sample
import json

# Create your views here.


with open('static/data/main_menu_links.json', 'r', encoding='utf-8') as mml:
    main_menu_links = json.load(mml)

content = {
    'main_menu_links': main_menu_links
}


def index(request: HttpRequest):
    with open('static/data/trending_products.json', 'r',
              encoding='utf-8') as tp:
        trending_products = json.load(tp)
    with open('static/data/new_products.json', 'r', encoding='utf-8') as np:
        new_products = json.load(np)
    with open('static/data/exclusive_products.json', 'r',
              encoding='utf-8') as ep:
        exclusive_products = json.load(ep)
    with open('static/data/promo_products.json', 'r', encoding='utf-8') as pp:
        promo_products = json.load(pp)
    content['title'] = 'главная'
    content['trending_products'] = \
        sample(trending_products, len(trending_products))
    content['exclusive_products'] = \
        sample(exclusive_products, len(exclusive_products))
    content['new_products'] = \
        sample(new_products, len(new_products))
    content['promo_products'] = \
        sample(promo_products, len(promo_products))
    return render(request, 'mainapp/index.html', content)


def products(request: HttpRequest, current_product_category='all'):
    with open('static/data/trending_products.json', 'r',
              encoding='utf-8') as tp:
        trending_products = json.load(tp)
    with open('static/data/catalog_menu_links.json', 'r',
              encoding='utf-8') as cml:
        catalog_menu_links = json.load(cml)
    with open('static/data/promo_products.json', 'r', encoding='utf-8') as pp:
        promo_products = json.load(pp)
    content['title'] = 'каталог товаров'
    content['products_menu_category'] = catalog_menu_links
    content['trending_products'] = \
        sample(trending_products, len(trending_products))
    content['promo_products'] = \
        sample(promo_products, len(promo_products))
    content['current_product_category'] = current_product_category
    return render(request, 'mainapp/products.html', content)


def details(request: HttpRequest, color='red'):
    with open('static/data/trending_products.json', 'r',
              encoding='utf-8') as tp:
        trending_products = json.load(tp)
    with open('static/data/catalog_menu_links.json', 'r',
              encoding='utf-8') as cml:
        catalog_menu_links = json.load(cml)
    content['current_product_category'] = ''
    content['title'] = 'товар'
    content['products_menu_category'] = catalog_menu_links
    content['trending_products'] = \
        sample(trending_products, len(trending_products))
    content['color'] = color
    return render(request, 'mainapp/details.html', content)


def history(request: HttpRequest):
    content['title'] = 'временная страница'
    return render(request, 'mainapp/history.html', content)


def showroom(request: HttpRequest):
    content['title'] = 'временная страница'
    return render(request, 'mainapp/showroom.html', content)


def contacts(request: HttpRequest):
    with open('static/data/addresses.json', 'r', encoding='utf-8') as pp:
        addresses = json.load(pp)
    content['addresses'] = addresses
    content['title'] = 'контакты'
    return render(request, 'mainapp/contacts.html', content)
