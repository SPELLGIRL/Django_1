from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, \
    reverse, Http404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Basket
from mainapp.models import Product, MainMenu

main_menu_links = MainMenu.objects.all()

content = {
    'main_menu_links': main_menu_links
}


@login_required
def basket(request: HttpRequest):
    inner_content = {
        'title': 'Cart',
        'basket': Basket.objects.filter(user=request.user).order_by(
            'product__category')
    }

    inner_content = {**content, **inner_content}

    return render(request, 'basketapp/basket.html', inner_content)


@login_required
def basket_add(request: HttpRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)

    basket_product = Basket.objects.filter(user=request.user,
                                           product=product).first()

    if not basket_product:
        basket_product = Basket(user=request.user, product=product)

    basket_product.quantity += 1
    basket_product.save()

    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(
            reverse('catalog:product', args=[product.id]))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request: HttpRequest, pk: int):
    basket_product = get_object_or_404(Basket,
                                       user=request.user,
                                       product=pk)

    if basket_product.quantity == 1:
        basket_product.delete()
    else:
        basket_product.quantity -= 1
        basket_product.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request: HttpRequest, pk: int):
    basket_product = get_object_or_404(Basket, user=request.user, product=pk)
    basket_product.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
