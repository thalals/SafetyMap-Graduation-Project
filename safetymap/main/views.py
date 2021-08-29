from django.http.response import HttpResponse
from django.shortcuts import render
from folium import plugins
import folium
import geocoder     #import geojson
import json, requests

g = geocoder.ip('me')   #현재 내위치
# Create your views here.
def home(request) :
    map = folium.Map(location=g.latlng,zoom_start=15, width='100%', height='100%',)
    plugins.LocateControl().add_to(map)
    # plugins.Geocoder().add_to(map)

    maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 (folium)
    
    return render(request,'../templates/home.html',{'map' : maps})


def PathFinder(request) :
    coordinates=[]

    start_coordinate = getLatLng(request.POST.get('StartAddr'))
    end_coordinate = getLatLng(request.POST.get('EndAddr'))

    coordinates.append(start_coordinate)
    coordinates.append(end_coordinate)

    result = {"type":"feature" , "geometry" : {"type" : "point","coordinates" :coordinates}}

    map = folium.Map(location=start_coordinate,zoom_start=15, width='100%', height='100%',)
    plugins.LocateControl().add_to(map)

    folium.Marker(
        location=start_coordinate,
        popup=request.POST.get('StartAddr'),
        icon=folium.Icon(color="red"),
    ).add_to(map)

    folium.Marker(
        location=end_coordinate,
        popup=request.POST.get('EndAddr'),
        icon=folium.Icon(color="red"),
    ).add_to(map)

    maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 (folium)

    # return HttpResponse(json.dumps({'result' : result}), content_type='application/json')       #return ajax datatype -> json
    return render(request,'../templates/home.html',{'map' : maps})

def GetSpotPoint(request) :

    start_coordinate = getLatLng(request.POST.get('StartAddr'))
    end_coordinate = getLatLng(request.POST.get('EndAddr'))

    context = {'startaddr' : start_coordinate, 'endaddr' : end_coordinate}    
    # result = {"type":"feature" , "geometry" : {"type" : "point","coordinates" :coordinates}}
    # print('result : ',result)
    return HttpResponse(json.dumps(context), content_type='application/json')

def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
    headers = {"Authorization": "KakaoAK 894cfd738b31d10baba806317025d155"}
    result = json.loads(str(requests.get(url,headers=headers).text))
    match_first = result['documents'][0]['address']

    return float(match_first['y']),float(match_first['x'])