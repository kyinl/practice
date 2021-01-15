import requests
from bs4 import BeautifulSoup

KEY = '90%2F96a%2FqZQwcQFHkaXiSXZzRru%2FLvjHSOREmbnWrGLZYwxBfn9MT1GCS2uF%2BvXSanEnj%2B8yjWbBzkCGtfcy07Q%3D%3D'
URL = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=xml'

response = requests.get(URL).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[0]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')



# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
if 150 < dust:
    print('매우나쁨')
elif 80 < dust <= 150:
    print('나쁨')
elif 50 < dust <= 80:
    print('보통')
else:
    print('좋음')

