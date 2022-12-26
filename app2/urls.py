from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path('loganathan/',loganathan,name='loganathan'),
    path('gokul/',gokul,name='gokul'),
]