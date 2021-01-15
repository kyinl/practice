# json api 크롤링

import requests

name = 'kyungmin'
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json() # json() 메서드 호출
# print(type(response))
age = response['age']

print(f'{name}의 나이는 {age}살 입니다.')
