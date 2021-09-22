from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
        path('',views.adminstartor, name='manager'),
        path('/Mpath',views.PathFinder, name='manager_pathfinder'),
        path('/MSetSpot', views.GetSpotPoint, name='manager_getspotpoint'),
]