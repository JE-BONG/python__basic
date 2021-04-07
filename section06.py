# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter) :
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요

# 예제1
print('<함수 선언>')
def hello(world) :
    print('Hello', world)

hello("Python")
hello(7777)

print()
print('-----------------------------------')

# 예제2
# return 포함
print('<함수 return 포함>')
def hello_return(world):
    val = "Hello" + str(world)    # world가 str이 되어야 하기 때문에 str로 바꿔서 출력
    return val
str = hello_return('Python!!!!!') # 함수를 호출한 곳으로 매개변수를 보낸다.
print(str)
print()
print('-----------------------------------')

# 예제3 (다중 return) ★★★★★
print('<다중 return>')
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    y4 = x * 400
    return y1, y2, y3, y4

val1, val2, val3, val4 = func_mul(100)
print(val1)
print(val2)
print(val3)
print(val4)
print(val1, val2, val3)
print()
print('-----------------------------------')

# 예제4 (데이터 타입 변환)
print('<데이터 타입 변환>')
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print('<결과 and 타입 확인>')
print(lt, type(lt)) 
print()
print('----------------------------------')

# 예제4
# *args(tuple), *kwargs(dict)
# * 가 하나일 경우 : tuple로 받는다.
# **가 두개일 경우 : dict로 받는다.
# * 가 붙는 경우   : 매개변수가 몇개가 넘어 갈지 모를 때 사용(무한정 가능)
def args_func(*args):
    print(args)     # 무조건 출력
    # enumerate : 각 값마다 인덱스를 보여준다.
    for i,v in enumerate(args):
        print(i, v) # 튜플 형식으로 출력 (key, value)

args_func('kim') # enumerate를 통해 인덱스 까지 출력
args_func('kim','Park')
args_func('kim','Park','Lee')
print()
print('------------------------------------------')

# kwargs : 키워드 줄임말
# ** : dict()로 받는다.
def kwargs_func(**kwargs) :
    for k, v in kwargs.items():
        print(k, v)
    print(kwargs)
kwargs_func(name1='Kim', name2='park', name3='lee')
print()
print('-------------------------------------------')

# 전체 혼합
# *args(Tuple), **kwargs(dict) : 가변인자라 값이 있어도 , 없어도 된다.
print('<전체 응용 혼합>')
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)
print()
print('-------------------------------------------')

# 중첩 함수(클로저) / javaScripts : 재귀함수
# 파이썬 데코레이터 클로저★★★★★
print('<중첩 함수 클로저>')
def nested_func(num):
    def func_in_func(num):
        print(num)
    
    # 실제 출력은 nested_func() 함수에서 활용 / 내부 함수에서 출력 가능하게끔 들여쓰기 필수   
        print("in func")
    # 내부 함수인 func_in_func 함수 호출
    # 실제 출력문
    func_in_func(num + 10000) # 내부 함수 func_in_func를 호출해 print()문으로 최종값 출력

nested_func(10000)
print()
print('--------------------------------------------')

print('<예제 6 : hint>')
# def func_mul3(x: int) -> list : x는 int이고 list형식으로 반환한다.
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))

print()
print('---------------------------------------------')

print('<람다식 예제>')
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다(lambda)는 즉시 실행(Heap 초기화) -> 메모리 초기화
# 가독성이 떨어질 수 있는 단점
# 일반적 함수 -> 변수 할당

def mul_10(num : int) -> int :
    return num * 10

var_func = mul_10
# 출력
print(var_func(10))
# 타입 확인
print(type(var_func))
print('-----------------------------------------------')
print('<lambda>식 사용')

# lambda num : num: int와 동일★★★★★
lambda_mul_10 = lambda num: num * 10
print('>>>', lambda_mul_10(10))

print()
print('------------------------------------------------')
print('<함수를 매개변수로 넘겨서 사용>')
def func_final(x, y, func) : # func : func() 함수를 매개변수에 포함
    print( x * y * func(10))

func_final(10, 10, lambda_mul_10)

print(func_final(10, 10, lambda x: x * 1000)) # x값이 없어서 None 출력



