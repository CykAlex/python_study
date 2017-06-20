# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def add(request):
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))