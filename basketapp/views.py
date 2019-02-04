from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpRequest
from basketapp.models import Basket
from mainapp.models import Product

from mainapp.models import MainMenu

main_menu_links = MainMenu.objects.all()

content = {
    'main_menu_links': main_menu_links
}


def basket(request: HttpRequest):
    # products = Basket.objects.filter(user=request.user).values_list('product_id', flat=True)
    products = Product.objects.filter(
        id__in=Basket.objects.filter(user=request.user).values_list(
            'product_id', flat=True))
    inner_content = {
        'title': 'Cart',
        'products': products
    }

    inner_content = {**content, **inner_content}

    return render(request, 'basketapp/basket.html', inner_content)


def basket_add(request: HttpRequest, pk):
    product = get_object_or_404(Product, pk=pk)

    basket_product = Basket.objects.filter(user=request.user,
                                           product=product).first()

    if not basket_product:
        basket_product = Basket(user=request.user, product=product)

    basket_product.quantity += 1
    basket_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request: HttpRequest, pk):
    product = get_object_or_404(Product, pk=pk)

    basket_product = Basket.objects.filter(user=request.user,
                                           product=product).first()

    if basket_product:
        if basket_product.quantity == 1:
            basket_product.delete()
        else:
            basket_product.quantity -= 1
            basket_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
