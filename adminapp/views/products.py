from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def create(request: HttpRequest):
    return HttpResponse('action -> create')


def read(request: HttpRequest, id):
    return HttpResponse('action -> read')


def list_by_category(request: HttpRequest, category):
    return HttpResponse('action -> list')


def update(request: HttpRequest, id):
    return HttpResponse('action -> update')


def delete(request: HttpRequest, id):
    return HttpResponse('action -> delete')
