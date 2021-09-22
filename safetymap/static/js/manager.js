"use strict"
console.log('관리관리')
//csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');


var resultArray=[]; //출발지, 목적지 좌표
var shortestRoute=[];   //최단거리 좌표 정보

var input = document.getElementById("start_input");
input.onclick  = function(){
    new daum.Postcode({
        oncomplete: function(data) {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분입니다.
            
            // 도로명 주소의 노출 규칙에 따라 주소를 표시한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            var roadAddr = data.roadAddress; // 도로명 주소 변수
            var extraRoadAddr = ''; // 참고 항목 변수

            // 법정동명이 있을 경우 추가한다. (법정리는 제외)
            // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
            if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                extraRoadAddr += data.bname;
            }
            // 건물명이 있고, 공동주택일 경우 추가한다.
            if(data.buildingName !== '' && data.apartment === 'Y'){
               extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
            }
            // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
            if(extraRoadAddr !== ''){
                extraRoadAddr = ' (' + extraRoadAddr + ')';
            }
            
            // 우편번호와 주소 정보를 해당 필드에 넣는다.
            // document.getElementById('sample4_postcode').value = data.zonecode;
            // document.getElementById("sample4_roadAddress").value = roadAddr;
            // document.getElementById("sample4_jibunAddress").value = data.jibunAddress;
            document.getElementById("StartAddr").value = roadAddr;            
        }
    }).open();
};


var output = document.getElementById("end_input");
output.onclick = function(){
    new daum.Postcode({
        oncomplete: function(data) {
            var roadAddr = data.roadAddress; // 도로명 주소 변수
            var extraRoadAddr = ''; // 참고 항목 변수

            if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                extraRoadAddr += data.bname;
            }
            if(data.buildingName !== '' && data.apartment === 'Y'){
               extraRoadAddr += (extraRoadAddr !== '' ? ', ' + data.buildingName : data.buildingName);
            }
            if(extraRoadAddr !== ''){
                extraRoadAddr = ' (' + extraRoadAddr + ')';
            }
            
            //set value 도로명 주소
            document.getElementById("EndAddr").value = roadAddr;     
        }
    }).open();
};


// //길찾기 버튼 클릭
$("#find_botton").click(function(){
    shortestRoute=[]    //초기화
    document.getElementById('pathForm').submit();

    // $.ajax({
    //     type:'POST',
    //     url : Mpathfinder,
        
    //     data:{
    //         'StartAddr' : $('#StartAddr').val(), 
    //         'EndAddr' : $('#EndAddr').val(),
    //         'csrfmiddlewaretoken':  csrftoken,
    //     },
    
    //     success : (result) => {
    //         console.log(result)
    //         // var leaf_map=L.map('map').setView([result['start'][1],result['start'][0]], 15); //setview [위도,경도], 줌레벨
                            
    //         // L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom: 18}).addTo(leaf_map);
    //         // markers=L.marker([result['start'][1],result['start'][0]]).addTo(leaf_map);
    //         // markers=L.marker([result['end'][1],result['end'][0]]).addTo(leaf_map);
    //         document.getElementById('pathForm').submit();
    //     },
    // });
});
