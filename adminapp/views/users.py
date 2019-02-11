from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    return HttpResponse('action -> index')


def create(request: HttpRequest):
    return HttpResponse('action -> create')


def read(request: HttpRequest, id):
    return HttpResponse('action -> read')


def update(request: HttpRequest, id):
    return HttpResponse('action -> update')


def delete(request: HttpRequest, id):
    return HttpResponse('action -> delete')
