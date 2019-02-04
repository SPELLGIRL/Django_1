from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from .models import Product, Category, CatalogMenu, MainMenu, NewMenu, Address
from random import sample
import os

main_menu_links = MainMenu.objects.all()

content = {
    'main_menu_links': main_menu_links
}


def index(request: HttpRequest, current_product_category=''):
    if current_product_category != '':
        get_object_or_404(NewMenu,
                          category__name=current_product_category,
                          pk__gt=1)
        new_menu_products = list(Product.objects.filter(
            category__name=current_product_category))
    else:
        new_menu_products = list(Product.objects.filter(
            category__name=NewMenu.objects.first().category.name))

    new_menu_links = [{'title': NewMenu.objects.first().title,
                       'category__name': ''}] + list(
        NewMenu.objects.values('title', 'category__name')[1:])

    used_product_categories = ['trending', 'exclusive', 'promo', 'hot']

    inner_content = {
        'title': 'Main',
        'new_menu_links': new_menu_links,
        'current_product_category': current_product_category,
        'new_menu_products': new_menu_products,
    }
    for category in used_product_categories:
        _temp = list(Product.objects.filter(category__name=category))
        inner_content[category + '_products'] = sample(_temp, len(_temp))

    inner_content = {**content, **inner_content}
    return render(request, 'mainapp/index.html', inner_content)


def products(request: HttpRequest, current_product_category=''):
    if current_product_category != '':
        get_object_or_404(CatalogMenu,
                          category__name=current_product_category)
        catalog_menu_products = list(Product.objects.filter(
            category__name=current_product_category))
    else:
        catalog_menu_products = list(Product.objects.all())

    catalog_menu_links = [{'title': 'all',
                           'category__name': ''}] + list(
        CatalogMenu.objects.values('title', 'category__name'))

    used_product_categories = ['exclusive', 'promo']

    inner_content = {
        'title': 'Catalog',
        'catalog_menu_links': catalog_menu_links,
        'current_product_category': current_product_category,
        'catalog_menu_products': sample(catalog_menu_products,
                                        len(catalog_menu_products)),
    }

    for category in used_product_categories:
        _temp = list(Product.objects.filter(category__name=category))
        inner_content[category + '_products'] = sample(_temp, len(_temp))

    inner_content = {**content, **inner_content}

    return render(request, 'mainapp/products.html', inner_content)


def details(request: HttpRequest, product_id=None, color=None, size=None):
    current_product = get_object_or_404(Product, pk=product_id)

    if current_product.big_img_path and size is None:
        image_link = current_product.big_img_path.url
        if color:
            split = os.path.split(image_link)
            check_color = split[0] + str(color) + split[1]
            image_link = check_color if os.path.exists(
                check_color) else current_product.big_img_path.url
    elif current_product.small_img_path:
        image_link = current_product.small_img_path.url
    else:
        image_link = ''

    catalog_menu_links = list(CatalogMenu.objects.all())
    same_products = list(Product.objects.exclude(pk=product_id).filter(
        category__in=current_product.category.all()))
    inner_content = {
        'title': current_product.title,
        'products_menu_category':
            [{'title': 'all', 'category': ''}]
            + catalog_menu_links,
        'color': color,
        'current_product': current_product,
        'product_id': product_id,
        'img_link': image_link,
        'same_products': sample(same_products, len(same_products)),
        # 'product_desc': current_product.full_description,
        # 'product_price': current_product.price,
        # 'product_category': current_product.mark,
    }
    inner_content = {**content, **inner_content}

    return render(request, 'mainapp/details.html', inner_content)


def contacts(request: HttpRequest):
    addresses = list(Address.objects.all())
    inner_content = {
        'addresses': addresses,
        'title': 'Contacts',
    }
    inner_content = {**content, **inner_content}
    return render(request, 'mainapp/contacts.html', inner_content)
