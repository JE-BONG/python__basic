# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수
# 첫글자는 대문자로

# 클래스(객체), 인스턴스 차이 중요
# 네임스페이스  : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수(전체 공유)   : 직접 사용 가능★, 객체 보다 먼저 생성
# 인스턴스 변수(각자 공유) : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# self : this()
print('<클래스>')
# 선언
class 클래스명:
    pass

# 예제1
print()
print('----------------------------------------------------------')
print('<예제1>')
class UserInfo():
    # __init__(self) : 클래스를 최초 초기화 함수
    # 속성, 메소드

    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name : ", self.name)
userlist = UserInfo("토마스")
print(userlist.name)
print()

# namespace
print('<namespace>')
user1 = UserInfo("james") # user1에 할당될때 호출
print(user1.name)
user1.user_info_p()
user2 = UserInfo("alice")
print(user2.name)
user2.user_info_p()
    
print()
# 할당된 메모리 주소
print('<할당된 메모리 주소>')
print(id(user1)) 
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)
print()
print('------------------------------------------------------')
# 예제2
# self의 이해
print('<self의 이해>')
class SelfTest():
    def function1():     # 클래스 메소드 # self가 없기 때문에 안됨
        print('function1 called!') # self 없음
    def function2(self): # 인스턴스 메소드
        print(id(self))
        print('function2 called!') # self 있음
# 비교
self_test = SelfTest()

# self_test.function1() 
SelfTest.function1() # 클래스 이름으로 호출 self가 없기 때문
self_test.function2()# 인스턴스를 호출 or self가 있기 때문

# self가 없는 경우는 클래스가 직접 호출
# self가 있는 경우는 인스턴스가 호출

print(id(self_test))
SelfTest.function2(self_test)
print()
print('--------------------------------------------------------')

# 예제3
# 클래스 변수(self없음), 인스턴스 변수(self있음)
print('<예제3>')
class WareHouse:
    # 클래스변수 : self 없음
    # 연봉 인상율
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1
user1 = WareHouse('james')
user2 = WareHouse('alice')
user3 = WareHouse('tomas')
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)

# name 확인
print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1
print(user2.stock_num)
print(user3.stock_num)
