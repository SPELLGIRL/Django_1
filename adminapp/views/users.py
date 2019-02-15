from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from authapp.forms import RegisterForm, CustomUser
from adminapp.models.users import UserEditForm


@user_passes_test(lambda user: user.is_superuser)
def index(request: HttpRequest):
    users = CustomUser.objects.all()

    provider = Paginator(users, 10)

    try:
        products_provider = provider.page(users)
    except PageNotAnInteger:
        products_provider = provider.page(1)
    except EmptyPage:
        products_provider = provider.page(provider.num_pages)

    content = {
        'provider': products_provider,
    }

    return render(request, 'adminapp/users/index.html', content)


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        form = RegisterForm()

    content = {
        'title': 'Users create',
        'form': form
    }

    return render(request, 'adminapp/users/update.html', content)


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, id):
    user_profile = get_object_or_404(CustomUser, pk=id)
    content = {
        'title': 'User view',
        'user_profile': user_profile,
    }

    return render(request, 'adminapp/users/read.html', content)


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id):
    user_profile = get_object_or_404(CustomUser, pk=id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES,
                            instance=user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('adminapp:user_read', args=[user_profile.id]))
    else:
        form = UserEditForm(instance=user_profile)

    content = {
        'title': 'Users update',
        'form': form,
        'user_profile': user_profile,
    }

    return render(request, 'adminapp/users/update.html', content)


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    user_profile = get_object_or_404(CustomUser, pk=id)

    if request.method == 'POST':
        user_profile.is_active = False
        user_profile.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {
        'title': 'Users delete',
        'user_profile': user_profile,
    }

    return render(request, 'adminapp/users/delete.html', content)
