# 함수
# 특정 역할을 하는 코드의 집합
# 하나의 함수는 하나의 역할만 해야 한다.

# 함수 정의
# def funcname(parameter_list):
#    """
#    docstring # 설명서
#    """
#    pass # pass 지우고 코드작성

def sum(a, b):
    result = a + b
    return result # return 이 없으면 None을 리턴함.

    apple = a * b # return 이후의 코드 작동안함.

# 함수 실행
sum(1, 2)
print(sum(1, 2))

# 함수 실행 결과(return)값 변수에 할당
result = sum(1, 2)
print(result)

# 미니 실습) 주어진 양수 n
help(print)