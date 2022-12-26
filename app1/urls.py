from django.urls import path
from app1.views import *
app_name='something1'
urlpatterns=[
    path('muniraji/',muniraji,name='muniraji'),
    path('abishek/',abishek,name='abishek'),
]