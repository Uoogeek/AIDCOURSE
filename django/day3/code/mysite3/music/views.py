from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1_view(request):
    return HttpResponse('页面1')

def page2_view(request):
    return HttpResponse('页面2')

def page3_view(request):
    return HttpResponse('页面3')

def page4_view(request):
    return HttpResponse('页面4')

def page5_view(request):
    return HttpResponse('页面5')

def index_view(request):
    return HttpResponse('音乐首页')
