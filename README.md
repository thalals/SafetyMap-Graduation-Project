# 안전한 보행길 탐색 지도(개인 졸업작품)
### 🎨기술 스택
<p align='center'>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/jQuery-B5FCF?style=flat-square&logo=jQuery&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/python-5483B1?style=flat-square&logo=python&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/Django-232F3E?style=flat-square&logo=Django&logoColor=white"/></a> 
<img src="https://img.shields.io/badge/Mysql-47A248?style=flat-square&logo=Mysql&logoColor=white"/></a>
<img src="https://img.shields.io/badge/QGIS-BD8B13?style=flat-square&logo=QGIS%20AWS&logoColor=white"/></a> 
</p>


## 🚙결과물

<p align='center'>
  최단 경로(RED)
  안전 경로(BLUE)
    <img src="https://user-images.githubusercontent.com/42319300/142750851-e27d5dea-a09f-4a2c-bf76-d2c72790d62c.PNG" width="500px" /></br>
  Tile cost
     <img src="https://user-images.githubusercontent.com/42319300/142750858-91f88d52-3a81-489a-88d1-3bfe09479fe9.PNG" width="500px" />


</p>

## 📁배경
내 주위 사람이 어두운 길을 조금이라도 안전하게 왔으면서 싶어서


## 🧾활용 데이터
공공데이터 포털, 경기도 데어터셋, 도로명주소 전자지도
1. CCTV
2. 가로등
3. 보안등
4. 스마트 가로등
5. 치안센터
6. 편의점
7. 24 상가
8. 도로명주소(SHP)


## 📌근거
2019년 치안정책센터에서 가로등이 범죄에 미치는 영향에 조사한 결과를 근거로 개발을 시작

## ✨주요기능
최단경로와 안전경로 탐색
두 경로의 비교 결과를 사용자에게 제공

## ✨기능 구현
1. 출발지와 목적지 사이의 범위 지정
2. 해당 범위를 6각형의 Hexgrid로 map 구성
3. 2차원 평면에서 물체가 사각형보다 육각형으로 이동했을 때 조금 더 입체적인 움직임 표현이 가능
4. Astar 알고리즘을 이용
5. F값(Huristic + g(현재까지온거리)) 과 cost 값을 일정 비율로 TileCost를 설정

## 😤아쉬운점
1. 데이터가 충분하지 못해 갈 수 있는 길을 명확하게 판단하지 못함
2. 데이터베에스에서 데이터를 불러오는 시간이 오래걸림(약 2초)
3. 경로 탐색알고리즘의 성능이 예상에 미치지 못함(속도 저하)


