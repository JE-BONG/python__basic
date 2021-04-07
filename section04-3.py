# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 문자열 : 처음 등록 후 수정 불가
# List (순서o, 중복o, 수정,삭제 가능)
# java : List(순서o, 중복o)
a = []
b = list()
c = [1, 2, 3, 4]
# 자료형 상관없이 아무 타입이든 배열에 저장 가능
d = [10, 100, 'Pen', 'Banana', 'Orange']
# 중첩 List
e = [10, 100, ['Pen', 'Banana', 'Oragne']]

# 인덱싱
# 위에 각 a,b,c,d,e 에 담겨 있는 인덱스의 값(번호)을 호출
# 문자열은 한번 할당하면 변경할 수 없다.(인덱스를 가지고 있기 때문)
print(d[3])
print(d[-2])
print(d[0]+d[1]) # 인덱스 끼리 값 더하기
print(e[2][1])
print(e[-1][-2]) # 중첩 리스트에 있는 값 호출

# 슬라이싱
print(d[0:2])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0])+'hi')

# 리스트 수정/삭제
# 수정
c[0] = 77
print(c)

c[1:2] = [100,1000,10000]
print(c) # 배열을 초기에 얼마나 정했는지 상관없이 삽입 가능
c[1] = ['a', 'b', 'c'] # 1번 인덱스에 추가로 넣는다.
print(c)

# 삭제
# 삭제 del, remove, pop(호출 후 삭제)
del c[1]
print(c)
del c[-1]
print(c)
print()

# 리스트 함수
# append    : [] 리스트 형식으로 추가
# sort      : 정렬(True : 오름차순 / False : 내림차순)
# reverse() : 인덱스 반대로 출력
# insert(해당 인덱스, 추가할 값)
# remove()  : 번호 삭제 / 인덱스x
# pop()     : 마지막 객체 호출 후 삭제 / 인덱스o
# extend()  : 인덱스 마지막에 추가
y = [5, 2, 3, 4, 1]
print(y)
y.append(6) # y객체 뒤에 추가 6번 인덱스를 추가 / []리스트 형식으로 추가
print(y)
y.sort()    # 정렬 ASC
print(y)  
y.reverse() # 반대로 정렬 후 출력 DESC
print(y)
y.insert(2, 8) # 2번 인덱스에 8을 추가로 넣는다.
print(y)
y.remove(2) # 인덱스가 아닌 숫자 2를 지운다.
print(y)
y.remove(8)
print(y)
y.pop()     # 맨 마지막 객체를 호출 후 삭제 / Stack이라고도 함
print(y)

ex = [88, 77]
y.extend(ex) # 끝 부분에 추가 / append()도 가능
print(y) 
y.append(ex) # append는 리스트[] 형식으로 들어간다.
print(y)

# 튜플 (순서o, 중복o, | 수정/삭제 불가)
# 데이터 변경 불가 시 사용 : 중요한 데이터 사용
# List : [] / Tuple : () 
a = ()
b = (1,)
c = (1, 2, 3, 4)
# 튜플 안에 중첩 튜플 가능 / 수정 삭제 불가능
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

# 슬라이싱
print(d[2:]) # 2번인덱스부터 전체출력
print(d[2][0:2])

# 연산
print(c + d)
print(c * 3)
print()
print()

# 튜플 함수
z = (5, 2, 3, 1, 1)
print(z)
print(3 in z)     # z객체 안에 숫자 3이포함되어 있는지
print(z.index(1)) # index : 3이 있는 인덱스 숫자를 출력
print(z.count(1)) # count : 해당 숫자가 튜플안에 몇개 있는지 출력






















