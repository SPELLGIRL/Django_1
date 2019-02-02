from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from .models import Product, Category, CatalogMenu, MainMenu, NewMenu, Address
from random import sample
import os
from django.urls import reverse

main_menu_links = MainMenu.objects.all()

content = {
    'main_menu_links': main_menu_links
}


def index(request: HttpRequest, current_product_category=''):
    new_menu_links = [{'title': NewMenu.objects.first().title,
                       'category': ''}] + list(
        NewMenu.objects.all()[1:].values('title', 'category'))
    for i in new_menu_links[1:]:
        i['category'] = Category.objects.get(pk=i['category']).name
    trending_products = list(Product.objects.filter(category__name='trending'))
    new_products = list(Product.objects.filter(category__name='new'))
    exclusive_products = list(
        Product.objects.filter(category__name='exclusive'))
    promo_products = list(Product.objects.filter(category__name='promo'))

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


def details(request: HttpRequest, product_id=None, color=None, size=None):
    current_product = get_object_or_404(Product, pk=product_id)

    if current_product.big_img_path and size is None:
        image_link = current_product.big_img_path.url
        if color:
            split = os.path.split(current_product.big_img_path.url)
            image_link = split[0] + str(color) + split[1]

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
        'product_id': product_id,
        'img_link': image_link,
        'same_products': sample(same_products, len(same_products))
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
        'title': 'Contacts'
    }
    inner_content = {**content, **inner_content}
    return render(request, 'mainapp/contacts.html', inner_content)
