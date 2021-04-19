# 1. 재귀 용법
# - 함수 안에서 동일한 함수를 호출하는 형태
# - 재귀 함수는 전형적인 Stack의 형태
# # 참고 : 재귀 함수는 깊이가 1000회 이하가 되어야 한다.

# def factorial(num):
#     if num > 1 :
#         return num * factorial(num - 1)
#     else:
#         return num

# for num in range(10):
#     print(factorial(num))

# def multiple(num):
#     return_value = 1
#     for index in range(1, num+1):
#         return_value = return_value * index
#     return return_value

def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num - 1)

print(multiple(10))

import random
data = random.sample(range(100), 10)
def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])

print(sum_list(data))

# 회문 : 문장을 거꾸로 읽어도 제대로 읽은 것과 동일한 단어
# ex   : level
# 참고 - 리스트 슬라이싱
string = 'Dave'
# string[-1] = 'e'
# string[0] = 'D'
# string[1:-1] = 'av' # [1:-1] : -1은 맨뒤 인덱스 바로 앞에 인덱스까지 출력
# string[-1] = 'Dav'

def pailndrome(string):
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:
        return pailndrome(string[1:-1])
    else:
        return False

print(pailndrome(string))

# 연습
# 1. 정수n에 대해
# 2. n이 홀수이면 3 x n +1 을 하고
# 3. n이 짝수이면 n 을 2로 나눈다.
# 4. 계속 진행 후 n이 결국 1이 될 때까지 2와 3의 과정을 반복한다.
# n = 5
# def func(n):
#     print(n)
#     if n == 1:
#         return n
#     if n % 2 == 1:
#         return (func((3*n) +1))
#     else:
#         return (func(int(n / 2)))

# print(func(3))

# 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 func(n) 이라고 하면
# func(n)은 func(n-1) + func(n-2) + func(n-3)과 동일한 패턴 찾기
def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    
    return func(data-1) + func(data -2) + func(data -3)

print(func(3))















































        
         
















