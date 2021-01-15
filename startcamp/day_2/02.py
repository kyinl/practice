# Dictionary (딕셔너리)

my_home ={
    'location' : 'seoul',
    'area-code' : '02'
}

# 딕셔너리 원소 접근
# 1
print(my_home['location'])
# print(my_home['name']) 없는 것을 출력하려 해서 오류발생
# 2
print(my_home.get('location'))
print(my_home.get('name')) # None (없음에 대한 자료형)