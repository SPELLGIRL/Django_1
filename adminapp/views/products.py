from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):
    return HttpResponse('action -> create')


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, id):
    return HttpResponse('action -> read')


@user_passes_test(lambda user: user.is_superuser)
def list_by_category(request: HttpRequest, category):
    return HttpResponse('action -> list')


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id):
    return HttpResponse('action -> update')


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    return HttpResponse('action -> delete')
