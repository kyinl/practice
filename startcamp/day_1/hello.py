# 변수(variable) 사용
# 저장
greeting = '안녕하세요!'

print(greeting)
print(greeting)
print(greeting)
print(greeting)
print(greeting)

# 반복문 사용
# while
count = 0
while count < 5: # False가 될때까지 반복
    print(greeting)
    # print(count) 넣어서 count 값 확인해보기
    count = count + 1
print('while문 종료')
# for
for i in [1,1,2,2,5]: # 방법 1: 아무거나 5개인 리스트 사용.
    print(greeting)

for _ in range(5): # 방법 2: range 함수 사용. 안쓰이는 i 는 언더바로 대체
    print(greeting)