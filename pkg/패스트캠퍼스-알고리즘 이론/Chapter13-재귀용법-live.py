# 1. 재귀 용법(recursive call, 재귀 호출)
# - 함수 안에서 동일한 함수를 호출하는 형태
# - 재귀 함수는 전형적인 Stack의 형태
# 참고 : 재귀 함수는 깊이가 1000회 이하가 되어야 한다.

# 간단 예제
# 2! = 1 X 2
# 3! = 1 X 2 X 3
# 4! = 1 X 2 X 3 X 4
# 규칙 : n! = n X 함수명(n -1)
# 1. 함수(n)은 n > 1 이면 return n X 함수(n-1)
# 2. 함수(n)은 n < 1 이면 return n

# 1. 2! 경우
# 함수(2) 이면, 2>1 이므로 2 x 함수(1)
# 함수(1) 은 1이므로, return 2 x 1 = 2

# 2. 3! 경우
# 함수(3) 이면 3>1 이므로 3 x 함수(2)
# 함수(2) 이면 2>1 이므로 2 x 함수(1)
# 함수(1) 이면 1과 같으므로 return 1을 반환
# 즉, 3x2x1 이다.
# 참고 : pythontutor.com/live.html#mode=edit

# 방법1.
def factorial(num):
    if num > 1 :
        return num * factorial(num - 1)
    else:
        return num

for num in range(10):
    print(factorial(num))

# 방법2.
def factorial(num):
    if num <= 1:
        return num
    return_value = num * factorial(num -1)
    return return_value

# factorial(n)은 n - 1번의 factorial() 함수를 호출해서, 곱셈을 한다.
# 일종의 n-1번 반복문을 호출한 것과 동일
# factorial(n)함수를 호출할 때마다, 지역변수 n이 생성된다.
# 즉, 결국 둘 다 O(n)이다.

# 1부터 num까지의 곱을 출력
def multiple(num):
    return_value = 1
    for index in range(1, num+1): # 1부터 num(마지막인덱스전)+1 = 1~10
        return_value = return_value * index
    return return_value

# 1부터 num까지의 곱을 출력 (재귀)
def multiple(num):
    if num <= 1:
        return num
    return num * multiple(num - 1) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

print(multiple(10))

# 랜덤으로 출력되는 리스트의 합 구하기
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
# string[-1] = 'e'    # 마지막 인덱스
# string[0] = 'D'     # 첫번째 인덱스
# string[1:-1] = 'av' # [1:-1] : -1은 맨뒤 인덱스 바로 앞에 인덱스까지 출력
# string[-1] = 'Dav'

def pailndrome(string): 
    # 회문일 경우 True 반환
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:   
        return pailndrome(string[1:-1]) # ★ -1은 마지막인덱스가 아닌 마지막인덱스 앞 인덱스를 의미
    else:
    # 회문이 아닐 경우 False 반환
        return False

print(pailndrome(string))

# 연습
# 1. 정수n에 대해
# 2. n이 홀수이면 3 x n + 1 을 하고
# 3. n이 짝수이면 n 을 2로 나눈다.
# 4. 계속 진행 후 n이 결국 1이 될 때까지 2와 3의 과정을 반복한다.
n = 3
def func(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 1:
        return (func((3*n) +1))
    else:
        return (func(int(n / 2)))

print(func(3))
print('=======================================================')
# 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 func(n) 이라고 하면
# func(n)은 func(n-1) + func(n-2) + func(n-3)과 동일한 패턴 찾기
def func(data):
    # 데이터가 1개인 경우
    if data == 1:
        return 1
    # 데이터가 2개인 경우
    elif data == 2:
        return 2
    # 데이터가 3개인 경우
    elif data == 3:
        return 4
    
    # 데이터 개수가 4개 이상인 경우 찾는 방법
    return func(data-1) + func(data -2) + func(data -3) # 4 2 1 == 7   
    

print(func(5))















































        
         
















