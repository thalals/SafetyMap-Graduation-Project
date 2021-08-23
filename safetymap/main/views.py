from django.shortcuts import render
from folium import plugins
import folium
import geocoder     #import geojson

g = geocoder.ip('me')   #현재 내위치
# Create your views here.
def home(request) :
    map = folium.Map(location=g.latlng,zoom_start=15, width='100%', height='100%',)
    plugins.LocateControl().add_to(map)
    # plugins.Geocoder().add_to(map)

    maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 (folium)
    
    return render(request,'../templates/home.html',{'map' : maps})


def test(request) :
    
    return render(request, '../templates/kakaotest.html')