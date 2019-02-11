from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import user_passes_test
from mainapp.models import Category, Product
from adminapp.models.categories import CategoryEditForm


@user_passes_test(lambda user: user.is_superuser)
def index(request: HttpRequest):
    models = Category.objects.all()

    content = {
        'models': models,
    }

    return render(request, 'adminapp/categories/index.html', content)


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):

    if request.method == 'POST':
        form = CategoryEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = CategoryEditForm()

    content = {
        'title': 'Category create',
        'form': form,
    }

    return render(request, 'adminapp/categories/update.html', content)


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, id):
    model = get_object_or_404(Category, pk=id)
    content = {
        'title': 'Category list',
        'model': model,
        'products': model.products.all()[:5],
    }

    return render(request, 'adminapp/categories/read.html', content)


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id):
    model = get_object_or_404(Category, pk=id)

    if request.method == 'POST':
        form = CategoryEditForm(request.POST, request.FILES, instance=model)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))

    else:
        form = CategoryEditForm(instance=model)

    content = {
        'title': 'Category update',
        'form': form,
    }

    return render(request, 'adminapp/categories/update.html', content)


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    model = get_object_or_404(Category, pk=id)

    if request.method == 'POST':
        model.is_active = False
        model.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {
        'title': 'Category delete',
        'model': model
    }

    return render(request, 'adminapp/categories/delete.html', content)

