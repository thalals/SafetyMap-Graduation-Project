import collections

import math
import hexgrid 
import morton 
from main.models import *
import time

# 시간 측정 데코레이터 함수
def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = original_fn(*args, **kwargs)
        end_time = time.time()
        print("소요시간[{}]: {} sec".format(original_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn


Point = collections.namedtuple("Point", ["x", "y"])

result = []
Hmap = {}
@logging_time
def giveCost(grid, mapsize, startx, starty, endx, endy) :

    #x : lon(128), y : lat(37)
    loadpoint = Loadpoint.objects.filter(lon__range=(endx,startx),lat__range=(endy,starty)).order_by('lat')
    lamp = Lamp.objects.filter(lon__range=(endx,startx),lat__range=(endy,starty)).order_by('lat')
    cctv = Cctv.objects.filter(lon__range=(endx,startx),lat__range=(endy,starty)).order_by('lat')
    securitycenter = Securitycenter.objects.filter(lon__range=(endx,startx),lat__range=(endy,starty)).order_by('lat')
    alltimeshop = Alltimeshop.objects.filter(lon__range=(endx,startx),lat__range=(endy,starty)).order_by('lat')

    alltimeshop_distic = alltimeshop.values_list
    for coor in alltimeshop :
        print(coor.lat,coor.lon)
# hex 좌표로
@logging_time
def startSetting(start_coordinate, end_coordinate) :
    startX = start_coordinate[1]
    startY = start_coordinate[0]
    endX = end_coordinate[1]
    endY = end_coordinate[0]

    center=hexgrid.Point((float(startX)+float(endX))/2,(float(startY)+float(endY))/2)   #중앙
    rate = 110.574 / (111.320 * math.cos(37.55582994870823 * math.pi / 180))   #서울의 중앙을 잡고, 경도값에 대한 비율     
    grid = hexgrid.Grid(hexgrid.OrientationFlat, center, Point(rate*0.00010,0.00010), morton.Morton(2, 32)) #Point : hexgrid Size
    sPoint=grid.hex_at(Point(float(startX),float(startY)))      # hex_at : point to hex -> 출발지 Point -> hex좌표
    ePoint=grid.hex_at(Point(float(endX),float(endY)))          #목적지
    map_size=max(abs(sPoint.q),abs(sPoint.r))   #열col(q) 행row(r)
    
    real_hexMap_size = map_size+5   #ex) 21 (q,r)이 가지는 최대 절대값

    LeftCorner = (grid.hex_center(hexgrid.Hex(-(real_hexMap_size),0)).x ,grid.hex_center(hexgrid.Hex(0,-(real_hexMap_size))).y)
    RightCorner = (grid.hex_center(hexgrid.Hex((real_hexMap_size),0)).x ,grid.hex_center(hexgrid.Hex(0,(real_hexMap_size))).y)

    endx = RightCorner[0]
    endy = RightCorner[1]

    startx = LeftCorner[0]
    starty = LeftCorner[1]
    
    #DB 데이터 불러오기
    # 범위의 양수 계산을 위해 변수 startx,endx / starty,endy 초기화
    if(endx>startx) :
        temp = endx
        endx = startx
        startx = temp
    if(endy>starty) :
        temp = endy
        endy = starty
        starty = temp

    neighbor=[]
    neighbor =grid.hex_neighbors(grid.hex_at(center),real_hexMap_size) #hex_neighbor : type(Hex, int) -> list
    neighbor.append(grid.hex_at(center))
    # print(neighbor)

    for hex in neighbor :
        Hmap[hex]=0
    # print(Hmap)
    giveCost(grid,real_hexMap_size,startx,starty,endx,endy)  #cost


    # print(len(loadpoint))
    return result