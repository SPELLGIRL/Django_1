from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import Product, CatalogMenu, MainMenu, NewMenu, Address
from random import sample

from django.urls import reverse

main_menu_links = MainMenu.objects.all()

content = {
    'main_menu_links': main_menu_links
}


def index(request: HttpRequest, current_product_category='new'):
    new_menu_links = list(NewMenu.objects.all())
    for all_category in new_menu_links:
        if all_category.category.name == current_product_category:
            break
    else:
        return HttpResponseRedirect(reverse('home'))

    trending_products = list(Product.objects.filter(category__id=4))
    new_products = list(Product.objects.filter(category__id=1))
    exclusive_products = list(Product.objects.filter(category__id=3))
    promo_products = list(Product.objects.filter(category__id=6))

    inner_content = {
        'title': 'Main',
        'new_menu_links': new_menu_links,
        'trending_products': sample(trending_products, len(trending_products)),
        'exclusive_products': sample(exclusive_products,
                                     len(exclusive_products)),
        'new_products': sample(new_products, len(new_products)),
        'promo_products': sample(promo_products, len(promo_products)),
        'current_product_category': current_product_category
    }
    inner_content = {**content, **inner_content}
    return render(request, 'mainapp/index.html', inner_content)


def products(request: HttpRequest, current_product_category='all'):
    catalog_menu_links = list(CatalogMenu.objects.all())

    trending_products = list(Product.objects.filter(category__id=4))
    promo_products = list(Product.objects.filter(category__id=6))
    inner_content = {
        'title': 'Catalog',
        'products_menu_category':
            [{'title': 'all', 'category': 'all'}]
            + catalog_menu_links,
        'trending_products': sample(trending_products, len(trending_products)),
        'promo_products': sample(promo_products, len(promo_products)),
        'current_product_category': current_product_category
    }
    inner_content = {**content, **inner_content}

    for all_category in catalog_menu_links:
        if current_product_category == 'all' or all_category.category.name == current_product_category:
            return render(request, 'mainapp/products.html', inner_content)
    else:
        return HttpResponseRedirect(reverse('catalog'))


def details(request: HttpRequest, color='red'):
    trending_products = list(Product.objects.filter(category__id=4))
    catalog_menu_links = list(CatalogMenu.objects.all())
    inner_content = {
        'title': 'Product',
        'products_menu_category':
            [{'title': 'all', 'category': ''}]
            + catalog_menu_links,
        'trending_products': sample(trending_products, len(trending_products)),
        'color': color
    }
    inner_content = {**content, **inner_content}
    return render(request, 'mainapp/details.html', inner_content)


def contacts(request: HttpRequest):
    addresses = list(Address.objects.all())
    inner_content = {
        'addresses': addresses,
        'title': 'Contacts'
    }
    inner_content = {**content, **inner_content}
    return render(request, 'mainapp/contacts.html', inner_content)
