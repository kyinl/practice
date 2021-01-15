import requests
from bs4 import BeautifulSoup


# 1. url
url = 'https://finance.naver.com/marketindex/'

# 2. url 로 요청을 보낸 후 응답을 받는다.
response = requests.get(url).text # 텍스트 정보만 필요함.

# 3. 받은 응답을 예쁘게 꾸며준다.
data = BeautifulSoup(response, 'html.parser')

# 4. 꾸민 응답중에서 원하는 데이터를 선택한다.
result = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text # text만 선택
print(result)

