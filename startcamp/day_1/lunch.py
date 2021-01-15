# list(리스트) - pythonic

stores = ['새마을식당', '리춘시장', '스타벅스']
print(stores)
print(stores[1]) # 값이므로 대괄호와 따옴표 없이 출력

# random 모듈 및 함수 사용
# 모듈은 함수의 모임
import random

pick = random.sample(stores, 1)
print(pick) # 리스트이므로 대괄호와 따옴표 달고 출력.