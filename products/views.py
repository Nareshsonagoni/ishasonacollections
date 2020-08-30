from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('This is your products app')


def new(request):
    return HttpResponse('New Products')
