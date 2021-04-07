# 대표적인 데이터 구조6 - 해쉬 테이블

# 1. 해쉬 구조
# Hash Table : 키(key)에 데이터(value)를 저장하는 데이터 구조
# key를 통해 바로 데이터를 받아 올 수 있으므로, 속도가 획기적으로 빨라짐
# 파이썬 딕셔너리 타입이 해쉬 테이블의 예: key를 가지고 바로 데이터를 꺼냄
# 보통 배열로 미리 Hash Table 사이즈만큼 생성 후에 사용(공간과 탐색 시간을 맞바꾸는 기법)
# 단, 파이썬에서는 해쉬를 별도 구현할 이유가 없다
# 딕셔너리 타입을 사용하면 된다

# 2. 알아둘 용어
# 해쉬        : 임의 값을 고정 길이로 변환하는 것
# 해쉬 테이블 : 키 값의 연산에 의해 직접 전근이 가능한 데이터 구조
# 해상 함수   : key에 대해 산술 연산을 이용해 데이터 위취를 찾을 수 있는 함수
# 해쉬값 또는 해쉬 주소를 해싱 함수로 연산해서, 해쉬 값을 알아내고, 이를
# 기반으로 해쉬 테이블에서 해당 key에 대한 데이터 
# 슬롯 : 한개의 데이터를 저장할 수 있는 공간
# 저장할 데이터에 대해 key를 추출할 수 있는 별도 함수도 존재할 수 있다

# 3. 간단한 해쉬 예
# 3-1 hash Table만들기
# - 참고 : 파이썬 list comprehension - https://www.fun-coding.org/PL&OO5-2.html

# list comprehension
# range에 숫자를 차례로 i에 넘겨 0에 또 넘겨 list형식으로 만든다.★★
hash_table = list(0 for i in range(10)) 
print(hash_table)

# 3-2 초간단 해쉬 함수 만들기
# 다양한 해쉬 함수 고안 기법이 있으며, 가장 간단한 방식이 DiVision법(나누기를 통한 나머지값을 사용하는 기법-dir())
def hash_func(key):
    return key % 5
print(hash_func(8))

# 3-3 해쉬 테이블에 저장하기
# - 데이터에 따라 필요시 key 생성 방법 정의가 필요 : 각 데이터마다 첫글자를 ASCII코드로 key값 설정★
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord()  : 문자의 ASCII 코드 리턴★★
print('a의 ascii코드값:', ord('a'))
# index(): 해당 값 입력 시 해당값이 있는 인덱스 번호를 알려준다.
print(ord(data1[0])) # ex) A의 해당하는 ASCII코드값 : 65
print(ord(data1[0]), hash_func(ord(data1[0])))

# 해쉬 테이블에 값 저장 예
# data : value와 같이 data와 value를 넣으면, 해당 data에 대한 key를 찾아서
# 해당 key에 대응하는 해쉬주소에 value를 저장하는 예
def storage_data(data,value):
    key = ord(data[0])                # 65
    hash_address = hash_func(key)     # 주소 : hash_func(key)에서 나누고 나머지값이 저장
    hash_table[hash_address] = value  # hash_table에 인덱스 번호로 설정되고 해당 인덱스번호에 값이 들어간다.

# 해쉬 테이블에서 특정 주소의 데이터를 가져오는 함수
# dict()방식으로 넣는다.
storage_data('Andy','01011111111')
storage_data('Dave','01022222222')
storage_data('Trump','01033333333')

# 실제 데이터를 저장하고, 읽기
def get_data(data):
    key = ord(data[0]) # key : A -> 65
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('Andy')) # Andy가 가지고 있는 value값을 호출★

# 4. 자료 구조 해쉬 테이블의 장단점과 주요 용도
# - 장점
# 1. 데이터 저장/읽기 속도가 빠르다(검색 속도가 빠르다)
# 2. 해쉬는 키에 대한 데이터가 있는지 중복 확인이 쉽다★

# - 단점
# 1. 일반적으로 저장공간이 좀 더 많이 필요하다.
# 2. 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조 필요★

# - 주요 용도
# 1. 검색이 많이 필요할 경우★
# 2. 저장, 삭제, 읽기가 빈번한 경우
# 3. 캐시(쿠키) 구현 시 (중복 확인이 쉽기 때문)

# 5. 프로그래밍 연습
# 연습1. list 변수를 활용해서 해쉬 테이블 구현해보기
# 1. 해쉬 함수 : key % 8
# 2. 해쉬 키 생성 : hash(data)
# hash() : 파이썬 내장 함수★ (실행마다 값이 달라질 수 있다.)
print('---------------------------------------------------------------------')
print()

hash_table = list([0 for i in range(8)]) # 0~7 : 8개의 배열을 만든다.

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % len(hash_table) # 8개의 배열과 나누고 남은 값 출력

# 배열에 데이터 저장
def save_data(data, value):
    hash_address = hash_function(get_key(data)) # key값
    hash_table[hash_address] = value            # 해당 인덱스에 save_data를 호출한 value값이 들어간다.

def read_data(data):
    hash_address = hash_function(get_key(data)) 
    return hash_table[hash_address]             # 해당 인덱스에 있는 데이터value값 출력
    
save_data('Dave', '01011111111')
save_data('Alcie', '01022222222')
read_data('Dave')
print(hash_table) 
print(hash('Dave')) # hash값은 변경 될 수 있다.
print('hash_table길이:', len(hash_table))
print(read_data('Dave'))

# 6. 충돌(Collision) 해결 알고리즘(좋은 해쉬 함수 사용하기)
# - 해쉬 테이블의 가장 큰 문제는 충돌의 경우이다 이 경우를 해쉬충돌이라고 한다.

# 6-1. Chaining 기법(LinkedList기법을 통해 데이터를 추가로 뒤에 연결시켜 저장)
# - 개방 해쉬 또는 open Hashing기법 중 하나: 해쉬 테이블 저장공간 외의 공간 활용기법
# - 충돌 시 LinkedList기법을 통해 데이터를 추가로 뒤에 연결시켜 저장하는 방법★

# 6-2 Linear Probing 기법(★맨 처음 나오는 빈공간에 저장★/Linked List로 넣지 않음)
# 폐쇠 해슁 또는 Close Hashing 기법 중 하나 : 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
# 충돌이 일어나면 해당 hash address의 다음 address부터 a★맨 처음 나오는 빈공간에 저장★하는 기법
# - 저장공간 활용도를 높이기 위한 기법(빈 공간을 메우기때문에 활용도 갑)

# 연습3: 연습1의 해쉬 테이블 코드에 Linear Probling 기법으로 충돌해결 코드를 추가해보기
# 1. 해쉬 함수   : key % 8
# 2. 해쉬 키 생성: hash(data)

print('---------------------------------------------------------------------')
print()

hash_table = list([0 for i in range(8)])

def get_key(data) :
    return hash(data)

def hash_function(key) :
    return key % 8

def save_data(data, value) :
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 해쉬 주소에 데이터가 이미 저장되어 있다면
       # 내가 원하는 데이터인지 확인
       for index in range(hash_address, len(hash_table)): # 0 ~ 7           
           if hash_table[index] == 0 :                # for문을 통해 인덱스마다 빈곳을 확인 후 index값이 0이면 빈곳이기 때문에
              hash_table[index] == [index_key, value] # 해당 인덱스에 key,value값 저장
              return
           elif hash_table[index][0] == index_key : # key값이 동일한게 존재하다면
               hash_table[index][1] = value         # 해당 인덱스에 값만 업데이트 시켜준다.
               return
    else : # 해쉬 주소에 데이터가 저장되어 있지 않다면
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:   # 해쉬 테이블에 값이 저장된 주소가 없다면
        for index in range(hash_address,len(hash_table)):
            if hash_table[index] == 0 : # 데이터가 저장된 적이 없다면
                return None
            elif hash_table[index][0] == index_key : # 만약 찾고자 하는 데이터라면
                return hash_table[index][1]          # 데이터에 있는 value값 출력
    else :
        return None

print(hash('dk') % 8)
print(hash('da') % 8)

save_data('dk','01099999999')
save_data('da','01055555555')
read_data('dk')
            
print('---------------------------------------------------------------------')
print()

# 6-3 빈번한 충돌을 개선하는 기법
# - 해쉬 함수를 재정의 및 해쉬 테이블 저장공간을 확대
# - 기존의 hash_table을 두배로 늘려주는것이 일반적
# ex)
hash_table = list([None for i in range(16)])

def hash_function(key):
    return key % 16

# 참고 : 해쉬 함수와 키 생성 함수
# 파이썬의 hash() 함수는 실행마다 값이 달라질 수 있다
# 유명한 해쉬 함수들이 존재 : SHA(Secure Hash Algorithm, 안전한 해시 알고리즘)
# - 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용가능)

# SHA-1(import hashlib 필수)
print('SHA-1')
import hashlib
data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(b'test')       # test를 byte로 변경해야 해쉬로 사용가능 
hex_dig = hash_object.hexdigest() # hexdigest() : 변경된 hash_object객체를 16진수로 변환
print(hex_dig)
print()

# SHA-256
print('SHA-256')
import hashlib
data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(b'test')       # test를 byte로 변경해야 해쉬로 사용가능 
hex_dig = hash_object.hexdigest() # hexdigest() : 변경된 hash_object객체를 16진수로 변환
print(type(hex_dig)) # 문자열로 출력
print(int(hex_dig, 16) % 8) 

# 연습4 : 연습2의 Chaining 기법을 적용한 해쉬 테이블 코드에 키 생성 함수를 
#         sha256 해쉬 알고리즘을 사용하도록 변경해보기
# 1. 해쉬 함수   : key % 8
# 2. 해쉬 키 생성: hash(data)


print('---------------------------------------------------------------------')
print()

import hashlib
hash_table = list([0 for i in range(8)])

def get_key(data) :
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) # hex_dig는 문자열로 출력되기 때문에 int형 16진수로 변환

def hash_function(key) :
    return key % 8

def save_data(data, value) :
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0: # 해쉬 주소에 데이터가 이미 저장되어 있다면
       # 내가 원하는 데이터인지 확인
       for index in range(hash_address, len(hash_table)): # 0 ~ 7           
           if hash_table[index] == 0 :                # for문을 통해 인덱스마다 빈곳을 확인 후 index값이 0이면 빈곳이기 때문에
              hash_table[index] == [index_key, value] # 해당 인덱스에 key,value값 저장
              return
           elif hash_table[index][0] == index_key : # key값이 동일한게 존재하다면
               hash_table[index][1] = value         # 해당 인덱스에 값만 업데이트 시켜준다.
               return
    else : # 해쉬 주소에 데이터가 저장되어 있지 않다면
        hash_table[hash_address] = [index_key, value]

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:   # 해쉬 테이블에 값이 저장된 주소가 없다면
        for index in range(hash_address,len(hash_table)):
            if hash_table[index] == 0 : # 데이터가 저장된 적이 없다면
                return None
            elif hash_table[index][0] == index_key : # 만약 찾고자 하는 데이터라면
                return hash_table[index][1]          # 데이터에 있는 value값 출력
    else :
        return None

# 값이 고정되어 변경되지 않는다.
print(get_key('db') % 8)
print(get_key('da') % 8)
print(get_key('dc') % 8)

# 데이터 추가 및 출력
save_data('da', '010333333333')
save_data('db', '010010102022')
print(read_data('db'))

print('---------------------------------------------------------------------')
print()
print(hash('dq'))

# 7. 시간 복잡도 ( O(1) )
# - 일반적인 경우(Collision/(충돌)이 없는 경우)는 O(1)        : 상수의 시간(충돌이 없는 경우)
# - 최악의 경우(Collision(충돌)이 모두 발생하는 경우)는 O(n) : 충돌이 발생할 경우
# 해쉬 테이블의 경우, 일반적인 경우를 기대하고 만들기 때문에, 시간 복잡도는 O(1) 이라고 말할 수 있음

# 검색해서 해쉬 테이블의 사용 예
# 16개의 배열에 데이터를 저장하고 검색할 때 O(n)
# 16개의 데이터 저장공간을 가진 위의 해쉬 테이블에 데이터를 저장하고, 검색할 때 O(1)











