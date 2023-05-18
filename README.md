# 안전 보행길 탐색 지도(개인 졸업작품)

### 📁 구현 배경
어두운 밤, 가족들이 “조금 더 안전하게 거리를 다니면 좋겠다” 라는 생각에서 시작했습니다.

### 🚙결과물

<p align='center'>
  <span>
    <h5>최단 경로(RED) 안전 경로(BLUE)</h5></br>
    <img src="https://user-images.githubusercontent.com/42319300/142750851-e27d5dea-a09f-4a2c-bf76-d2c72790d62c.PNG" width="800px" />
  </span>
  
  <span>
  <h4> Tile cost</h4>
     <img src="https://user-images.githubusercontent.com/42319300/142750858-91f88d52-3a81-489a-88d1-3bfe09479fe9.PNG" width="600px" />
  </span>
</p>

### 🎨 기술 스택
- Django, Python
- MySql
- QGIS
- JavaScript, Leaflet.js

### 🎨 사용한 라이브러

- geocoder : 위치 좌표 변환</br>
- leaflet.js : 지도 프레임워크</br>
- hexgrid-py : 육각(hexagon) 그리드 구현</br>
- haversine : 좌표간 거리측정</br>

### 🧾활용 데이터
공공데이터 포털, 경기도 데어터셋, 도로명주소 전자지도
1. CCTV
2. 가로등
3. 보안등
4. 스마트 가로등
5. 치안센터
6. 편의점
7. 24 상가
8. 도로명주소(SHP)


### 📌근거
- 2019년 치안정책센터에서 가로등이 범죄에 미치는 영향에 조사한 결과를 근거로 개발을 시작

### ✨주요기능
1. 최단경로와 안전경로 탐색
2. 두 경로의 비교 결과를 사용자에게 제공

### ✨기능 구현 시나리오
1. 출발지와 목적지 사이의 범위 지정
2. 해당 범위를 6각형의 Hexgrid로 map 구성
3. 2차원 평면에서 물체가 사각형보다 육각형으로 이동했을 때 조금 더 입체적인 움직임 표현이 가능
4. Astar 알고리즘을 이용
5. F값(Huristic + g(현재까지온거리)) 과 cost 값을 일정 비율로 TileCost를 설정

### 😤아쉬운점
1. 데이터가 충분하지 못해 갈 수 있는 길을 명확하게 판단하지 못함
2. 데이터베에스에서 데이터를 불러오는 시간이 오래걸림(약 2초)
3. 경로 탐색알고리즘의 성능이 예상에 미치지 못함(속도 저하)


