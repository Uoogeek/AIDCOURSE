#file:bookstore/views

from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def add_view(request):
    try:
        #方法１
       # abook = models.Book.objects.create(title='c++',price=68)
        #return HttpResponse('添加图书成功')
        #方法２
        abook = models.Book(price=98)
        abook.title = '西游记'
        abook.save()
        return HttpResponse('添加图书成功')
    except Exception as err:
        return  HttpResponse('添加图书失败')
