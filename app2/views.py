from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def loganathan(request):
    return HttpResponse('This is first view on app2')
def gokul(request):
    return HttpResponse('This is second view on app2')