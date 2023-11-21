from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vasu(request):
    return HttpResponse('hii maya')
def maya(request):
    return HttpResponse('hlo di')

    
