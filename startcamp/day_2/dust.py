import requests
from pprint import pprint # pprint 모듈 안에서 pprint 함수 불러옴

# 미리보기의 전체 url: http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=90%2F96a%2FqZQwcQFHkaXiSXZzRru%2FLvjHSOREmbnWrGLZYwxBfn9MT1GCS2uF%2BvXSanEnj%2B8yjWbBzkCGtfcy07Q%3D%3D&returnType=json&numOfRows=5&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0
key = '90%2F96a%2FqZQwcQFHkaXiSXZzRru%2FLvjHSOREmbnWrGLZYwxBfn9MT1GCS2uF%2BvXSanEnj%2B8yjWbBzkCGtfcy07Q%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sido_name = '서울'
ver = '1.0'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_name}&ver={ver}'

response = requests.get(url).json()
# pprint(response) # 예쁘게 출력


# stationName의 미세먼지 농도는 pm10Value입니다. 라는 메세지를 출력하시오.
station_name = response['response']['body']['items'][0]['stationName'] # 미리보기 페이지에서 각각 접고 펴보면서 구조 파악하기
dust = response['response']['body']['items'][0]['pm10Value']

print(f'{station_name}의 미세먼지 농도는 {dust}입니다')