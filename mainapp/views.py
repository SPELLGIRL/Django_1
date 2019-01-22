from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def details(request):
    return render(request, 'mainapp/details.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
