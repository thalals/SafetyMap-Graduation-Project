from django.http.response import HttpResponse
from django.shortcuts import render
from folium import plugins
import folium
import geocoder     #import geojson
import json, requests
from main.models import *
import collections

from main import RouteSearch
g = geocoder.ip('me')   #현재 내위치
Point = collections.namedtuple("Point", ["x", "y"])

#관리자 페이지 (시각화 용)
def adminstartor(request) :
    map = folium.Map(location=g.latlng,zoom_start=15, width='100%', height='100%',)
    plugins.LocateControl().add_to(map)
    # plugins.Geocoder().add_to(map)

    maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 (folium)
    return render(request,'../templates/adminstartor.html',{'map' : maps})

def PathFinder(request) :
    SafeData=[]
    
    start_coordinate = getLatLng(request.POST.get('StartAddr'))
    end_coordinate = getLatLng(request.POST.get('EndAddr'))

    print("start : ",start_coordinate, "\nend : ", end_coordinate)

    # 구여 범위 내 db 정보 (cost)
    #-----------------return hex corner ---------------------
    RouteSearch.startSetting(start_coordinate, end_coordinate)
    
   
    # ---------------------------안전 루트--------------------------------------
    # 포인트 형태의 리스트 반환

    # SafeData = RouteSearch.setPoint(start_coordinate,end_coordinate)

     #-----------------------------맵핑-----------------------------------------
    map = folium.Map(location=start_coordinate,zoom_start=15, width='100%', height='100%',) 
    
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
    
    plugins.LocateControl().add_to(map)

    maps=map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 (folium)

     
    return render(request,'../templates/adminstartor.html',{'map' : maps})
 
    # return HttpResponse(json.dumps({'start' : start_coordinate, 'end':end_coordinate}))

def GetSpotPoint(request) :
    
    start_coordinate = getLatLng(request.POST.get('StartAddr'))
    end_coordinate = getLatLng(request.POST.get('EndAddr'))

    context = {'startaddr' : start_coordinate, 'endaddr' : end_coordinate}    

    return HttpResponse(json.dumps(context), content_type='application/json')

def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query='+addr
    headers = {"Authorization": "KakaoAK 894cfd738b31d10baba806317025d155"}
    result = json.loads(str(requests.get(url,headers=headers).text))
    match_first = result['documents'][0]['address']

    return float(match_first['y']),float(match_first['x'])