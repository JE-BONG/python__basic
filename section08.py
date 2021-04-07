# Section08
# 파이썬 모듈(클래스)과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용 1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)

# 사용 2(클래스)
from pkg.fibonacci import *

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)

Fibonacci.fib(500)

# 사용 3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)

print("ex1 : ", fb.fib2(1600))
print("ex1 : ", fb().title)

# 사용 4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용 5(함수)
from pkg.calculations import div as d
print("ex5 : ", int(d(100, 10)))

# 사용 6
import pkg.prints as p
import builtins # 어떤 개발도구를 사용했는지 알려준다 / 내장객체
p.prt1()
p.prt2()
print(dir(builtins))