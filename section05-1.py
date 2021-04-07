# Section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

# boolean타입
print('<Type 결과>')
print(type(True))
print(type(False))
print()
print('-----------------------------------------------')
print('<ex>')
# ex1)
if True :
    print('yes')

# ex2)
if False :
    print('no')

# ex3)
if False :
    print('no')
else :
    print('Yes2')

# 관계 연산자
# >, >=, <, <=, ==, !=
print()
print('-----------------------------------------------')
print('<관계 연산자>')
a= 10;
b= 0;
print(a == b) # False
print(a != b) # True
print(a > 10) # True
print(a >= b) # True
print(a < b)  # False
print(a <= b) # False

# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1(True)
# 거짓 : "", [], (), {}, 0(False)
city = ""
# city가 비어 있지 않은지
if city :
    print('True')
else : 
    print('False')
print()
print('---------------------------------------------------')

# 논리 연산자
# and or not
print('<논리 연산자>')
a = 100
b = 60
c = 15

print('and(모두 만족 시 출력) : ', a > b and b > c) 
print('or(하나라도 만족 시 출력) :', a > b or c > b)
print('not(반대로 생각) :', not a > b)
print(not False)
print(not True)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용★

# ex1 ) : false
# why ? : 5+10 = 10 true / 7+3 = 10은 맞지만 not조건 때문에 ==이 아닌 != 으로 false출력되기
#         때문에 false가 우선값이기 때문에 false출력
print('ex1 :', 5+10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A' :
    print('합격하셨습니다.')
else :
    print('죄송합니다. 불합격입니다.')

print()
print('--------------------------------------------------')
print('<다중 조건문>')
# 다중 조건문
num = 75
if num >= 90 :
    print('num 등급 A : ', num)
elif num >= 80 :
    print('num 등급 b : ', num)
elif num >= 70 :
    print('num 등급 c : ', num)
else :
    print('num 등급 : 꽝')
print()
print('--------------------------------------------------')
# 중첩 조건문
print('<중첩 조건문>')
age = 27
height = 175
if age >= 20:
    if height >= 170:
        print('A지망 지원 가능')
    elif heigth >= 160:
        print('B지망 지원 가능')
    else:
        print('지원 불가')
else:
    print('20세 이하는 지원이 불가능 합니다.')