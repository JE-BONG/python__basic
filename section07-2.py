# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1 
# 상속 기본 / 자바는 다중 상속 불가능
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모 
print('<상속 : inheritance (다중상속 가능) >')
class Car():
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp,color)
        self.car_name = car_name

    def show_model(self) -> None : # None : 리턴값이 없다?
        return "Your Car Name : %s" % self.car_name
    
    def show(self) : # super클래스에도 있는 클래스
        # 부모메소드까지 호출 시
        print(super().show())
        return 'Car Info : %s %s %s' %(self.car_name, self.type, self.color)

# 일반 사용
print()
print('<일반 상속 사용방법>')
model1 = BmwCar('520d', 'sedan', 'red')
print('색상 :', model1.color)        # super에서 가져온 것
print('타입 :', model1.type)         # super에서 가져온 것
print('이름 :', model1.car_name)     # sub  에서 가져온 것
print(model1.show())       # super에서 가져온 것
print(model1.show_model()) # sub에서 가져온 것
print(model1.__dict__)     # dict 형식으로 데이터 넣은 것 출력
print()
# Method Overriding(오버라이딩)
# 오버라이딩 : 부모 메소드를 재정의 하는 것 / Object 클래스에서 상속
# 오버로딩   : 매개변수만 그대로 / 모두 변경 가능
# java : 메소드명, 매개변수, 타입 모두 동일해야 가능
print('<오버라이딩>')
model2 = BenzCar('220d', 'suv', 'white')
print(model2.show())

# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())
print()
# Inheritance Info(상속 정보 -> 리스트 타입으로 출력)
print('mro()함수 : 상속받은 순서 출력')
print(BmwCar.mro())
print(BenzCar.mro())

# 예제2
# 다중 상속
class X(object):
    pass # pass : 나중에 구현하겠다는 의미 / 안쓰면 컴파일 에러

class Y() :
    pass

class Z() :
    pass

class A(X, Y) :
    pass

class B(Y, Z) :
    pass

class M(B, A, Z) :
    pass 

print(M.mro())
print(A.mro())





















