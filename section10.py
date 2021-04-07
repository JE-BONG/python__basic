# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임)프로세스에서 발생하는 
# 예외 처리도 중요
# linter : 코드 스타일 , 문법 체크

# SyntaxError : 문법이 잘못된 문법
# print('Test) 

# print('Test)
# if True
#     pass
# x => y  

# NameError : 참조변수 없음
a = 10 
b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
print(x[0])
# print(x[3]) # list index out of range

# keyError 
dic = {'name':'james', 'age':33, 'city':'seoul'}
# print(dic.[hobby])
# get★메소드를 통해 key를 찾는다 없는 경우 에러가 아닌 None 출력
print(dic.get('hobby')) 

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 시에 예외
import time
print(time.time())
# print(time.month()) # module'time' has no attrivute 'month' 예외 발생

# ValueError : 참조 값이 없을 때 발생
# 에러 구문  : x not in list 
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError 
# f = open('test.txt', 'r') # 예외 발생

# TypeError
x = [1, 2, 3]
y = (1, 2, 3)
z = 'test'

# print(x + y) # list와 tuple는 타입이 안맞아서 오류
# print(x + z)
print(x + list(y)) # 예외 형변환으로 출력가능

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 RuntimeError 예외 발생 시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try    : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else   : 에러가 발생하지 않았을 경우 실행
# finally: 무조건 실행되는 구문

# 예제1
print()
print('-------------------------------------------------')
print('<예제1>')

name = ['kim', 'lee', 'park']

try :
    z = 'kim' # cho : 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except : # 어떤 에러가 발생할 지 모르면 except만 작성
    print('Not Found it! - Occurred Error!')
else : # try 문이 정상 작동 시 출력
    print('Ok! else') 

# 예제2
print()
print('-------------------------------------------------')
print('<예제2>')

try :
    z = 'jin' # cho : 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except :
    print('Not Found it! - Occurred Error!')
else : # try 문이 정상 작동 시 출력
    print('Ok! else') 

# 예제3
print()
print('-------------------------------------------------')
print('<예제3>')

try :
    z = 'jin' # cho : 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except :
    print('Not Found it! - Occurred Error!')
else : 
    print('Ok! else')    # try 문이 정상 작동 시 출력
finally : 
    print('finally Ok!') # 정상/비정상 상관없이 출력

# 예제4
print()
print('-------------------------------------------------')
print('<예제4>')

try :
    print('Try')
finally : # 결과와 상관없이 출력
    print('Ok Finally!!!!')

# 예제5
print()
print('-------------------------------------------------')
print('<예제5>')

try :
    z = 'kim' # cho : 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l: # value 에러 발생 시 출력
    print(l)
except IndexError: # index 에러 발생 시 출력
    print('Not Found it! - Occurred Error!')
except Exception:  # 위 모든 예외가 잡지 못하면 해당 문구 출력
    print('Not Found it! - Occurred Error!')
else : 
    print('Ok! else')    # try 문이 정상 작동 시 출력
finally : 
    print('finally Ok!') # 정상/비정상 상관없이 출력   

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생
# raise : 즉 에러문구를 본인이 재정의 하는 것★★
print()
print('-------------------------------------------------')
print('<예제6>') 

try :
    a = '333'
    if a == 'Kim' :
        print('Ok 허가')
    else :
        # ValueError : 참조 값이 없을 때 나오는 에러 문구
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else :
    print('Ok!')

































































