# 데이터 타입
print('<데이터 타입>')
v_str1 = "Niceman(문자열)"
v_bool = True
v_str2 = "Good boy(문자열)"
v_float = 10.3
v_int = 7
#====================================================
# 딕셔너리(dict) : map처럼 key와 value로 구분
v_dict = {
    "name" : "Kim",
     "age" : 25 
}
#====================================================
# 튜플(tuple) : 불변한 순서가 있는 객체의 집합 / java : list
#        한번 생성되면 값을 변경할 수 없다.
v_tuple = 3, 5, 7
v_list = [3, 5, 7]
v_set = {7, 8, 9}
#====================================================
# type : 어떤 데이터 타입인지 알려준다
print(type(v_tuple))
print(type(v_list))
print(type(v_set))
print(type(v_float))
print(type(v_str2))

i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999999999
big_int2 = 777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5  # 0.5를 의미
f4 = 10. # 10.0을 의미

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2) # 제곱을 의미
print(f3 + i2)

result = f3 + i2
print(result, type(result))

a = 5.  # 5.0 실수를 의미
b = 4
c = 10
print(type(a), type(b))
result2 = a + b
print(result2) # 실수로 출력

#====================================================
# 형 변환
# int, float, complex(복소수)
print(int(result2)) # 실수 -> int형으로 데이터 타입 변환
print(float(c))     # 정수 -> float으로 데이터 타입 변환
print(complex(3))   # 복소수-> 
# 어떤 데이터 타입이든 정수형으로 자동 형 변환
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))

#====================================================
# 단항 연산자
y = 100
y *= 100
print(y)

#====================================================
# 수치 연산 함수
# https://docs.python.org/3/library/math.html
print(abs(-7))
n , m = 10, 20 # n : 10 , m : 20
# divmod(나눈값, 나머지값)
# java : /, %
# ex : 100에서 8을 나눈 값 : 12
#    : 96에서 나머지 4는 8자리에 들어온다
n, m = divmod(100, 8)
print(n,m)

import math
print(math.ceil(5.1))
print(math.floor(3.874))





















