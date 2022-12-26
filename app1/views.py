from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def muniraji(request):
    return HttpResponse('This is first view on app1')

def abishek(request):
    return HttpResponse('This is second view on app1')