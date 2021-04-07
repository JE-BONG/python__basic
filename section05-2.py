# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문  : for, while
print('<기본반복문 : for, while>')
print()

print('<while>')
v1 = 1 
while v1 < 11 : # 조건이 맞을 경우만 출력 # 11전 까지 출력
    print('v1 is :', v1)
    v1 += 1
print()
print('-----------------')
# v2 : 초기값이라 0
print('<for>')
for v2 in range(10) : # range : 10전까지 값 출력
    print('v2 is :', v2)
print('-----------------')
# range(시작값, 마지막값의 그 전의 값)
print('<for> range(시작값, 마지막인덱스전 값)')
for v3 in range(1,11):
    print('v3 is :', v3)
print('-----------------')
# 1 ~ 100합
# while : 조건에 맞는(True) 순간 while() 종료
print('<1 ~ 100까지의 합 구하기>')
sum1 = 0
cnt1 = 0
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 :', sum1)
print('<range>로 합 구하기')
print('1 ~ 100 :', sum(range(1,101)))
print('<range>로 짝수 합만 구하기')
# range(시작값, 끝나기전 값, 증감 단위)
print('1 ~ 100 :', sum(range(1, 101, 2)))

# 시퀀스(순서가 있는 자료형)반복 / 정렬 : sort()
# 문자열, 리스트, 튜플, 집합, 사전 
# iterable 리턴 함수 : range, reversed, enumberate, filter, map, zip 
# java : iterator()

names = ['kim', 'park', 'Cho', 'Choi', 'yoo']
# names가 name으로 순서대로 들어간다.
for name in names :
    print('you are : ', name)
print()
print('---------------------------------------------------')
# 문자열 : 한번 할당하면 수정 불가능(순서가 있고, 한글자가 자기자리에 있기 때문)
word = "dreams"
# java : for-each(타입 받을 객체명 : 객체)
for s in word :
    print("word", s)

# java : {"key" : value}
my_info = {
    'name' : 'kim',
    'age' : 33,
    'city' : 'seoul'
}
print()
print('---------------------------------------------------')
# 기본 값은 키
print('<key 만 출력>')
for key in my_info :
    print('my info', key)

# values()
print('---------------------------------------------------')
print('<value 만 출력 : values()>')
for value in my_info.values() :
    print('my info', value)

# key()
print('---------------------------------------------------')
print('<key 만 출력 : key()>')
for key in my_info.keys() :
    print('my info', key)

# items : key, values
print('---------------------------------------------------')
print('<key, value 모두 출력: items()>')
for k, v in my_info.items() :
    print('my info', k, v)

# 대문자 -> 소문자 / 소문자 -> 대문자
# isupper() : 대문자인지 확인 True/False 반환
# islower() : 소문자인지 확인 True/False 반환
print('---------------------------------------------------')
print('<대(uppper), 소(lower)로 변환 후 출력')
name = 'KennRY'
for n in name :
    if n.isupper() :
        print(n.lower())
    else :
        print(n.upper())
print('---------------------------------------------------')
print()

# break
# java : break;
print('<break>')
numbers = [14, 3, 4, 7 ,10 , 24, 33, 2, 37, 15, 34, 36, 38]
for num in numbers :
    if num == 33 :
        print('found : 33!')
        break
    else:
        print('not found : 33!')

# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행 / break에는 else문 실행 x)
for num in numbers :
    if num == 33 :
        print('found : 33!')
        break
    else:
        print('not found : 33!')
else :
    print("not found 33.....") # break문에 걸리지 않을 때만 출력 
print()
print('---------------------------------------------------')
# continue
print('<continue> : 맞는 값이 있을 때 다음 값 출력한다.')
lt = ["1", 2, 5, True, 4.3, complex(4)]

# lt(list)안에 실수형을 찾고 싶을 때
for v in lt :
    if type(v) is float : # v객체 중 float(실수) 형태의 값이 있는지
        continue          # continue를 만나면 다음 순회할 값을 출력
    print('타입 : ', type(v))
    
name = 'niceman'
print(reversed(name))
print(list(reversed(name))) # list : 순서, 중복o / 수정,삭제o
print(tuple(reversed(name)))
print(set(reversed(name)))  # set  : 순서, 중복x























