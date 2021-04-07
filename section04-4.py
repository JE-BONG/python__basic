# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 1. 딕셔너리(Dictionary) : 순서x 중복x 수정/삭제o : java : set()
# 1) 형식 : key, value  | java : map or json
# 2) 선언
print('==========================================')
print('<딕셔너리 : 순서x 중복x 수정,삭제 가능o>')
a = {'name' :'james', 'phone':'010-1111-1111', 'birth':'11-11-11'}
b = {0: 'Hello Pyhton', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}
print(type(a)) # 어떤 타입인지 출력
# 출력
print(a['name'])
# get() : 찾는 key값이 없으면 none
print(a.get('name'))
print(a.get('address'))
print(c.get('arr')[1:3])

# 딕셔너리 추가
print('=========================================')
print('<딕셔너리 추가>')
a['address'] = 'Seoul' # key / value 추가
print(a)
a['rank'] = [1, 3, 4]  # 리스트 형태도 추가 가능
a['rank2'] = (1,2,3)   # 튜플(순서o 중복o / 수정,삭제 x) 형태도 추가 가능
print(a)

# key, values, items 
# items : 'name':'james' 전체를 의미
print(a.keys()) # key 만 가져온다.
print(list(a.keys()))

temp = list(a.keys())   # a객체에 담긴 key값들을 list형식으로 temp객체에 담는다.
print(temp[1:3])        # temp에 담긴 인덱스 1번부터 3번까지 key값들이 출력

print(a.values())       # 값만 가져온다.
print(list(a.values())) # 리스트 안에 튜플이 들어가 있다.
print(2 in b)           # b객체에 2번 key가 있는지 true/false로 출력
print('name2' not in a) # a에 'name2'라는 key값이 있는지

# 집합(set : 순서x 중복x \ 자바set과 같음)
print('==========================================')
print('<set : 순서x중복x>')
a = set()
b = set([1, 2, 3]) # 리스트 형태로 넣는다.
c = set([1, 4, 5, 6, 6])
print(type(a))
print(c) # 중복이 안되기 때문에 6은 한번만 나온다.

t = tuple(b) # tuple로 변환
print(t)
l = list(b)  # list로 변환
print(l)
print('==========================================')
print('<교집합>')
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 방법1. 교집합을 구한다 s2와 같은 번호부터 출력
print(s1.intersection(s2)) 
# 방법2
print(s2 & s2) 
print('==========================================')
print('<합집합>')
# 4,5,6 은 출력되지 않는다 중복x이기 때문
print(s1 | s2)
print(s1.union(s2))
print('==========================================')
print('<차집합>')
print(s1 - s2)
print(s1.difference(s2))
print('==========================================')
print('<set추가/제거>')
print('<1.추가>')
s3 = set([7,8,10,15])
s3.add(18)
s3.add(7) # 중복을 허용하지 않기 때문에 추가가 안된다.
print(s3)
print()
print('<2.삭제>')
s3.remove(15)
print(s3)
print(type(s3))
