# 꼭 알아둬야 할 자료구조 : 스택(Stack)

# 데이터를 제한적으로 접근할 수 있는 구조
# ★ 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 궂
# 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 구조(LIFO)
# 큐(Queue) : FIFO(First in, First out)

# 1. 스택 구조
# 스택은 LIFO(last in first out) 또는 FILO(First in Last Out)
# LIFO : 마지막에 넣은 데이터를 가장 먼저 추출하는 데이터 관리 정책
# FILO : 처음에 넣은 데이터를 가장 마지막에 추출하는 데이터 관리 정책

# 1-1 대표적인 스택의 활용
# 컴퓨터 내부의 프로세스 구조의 함수 동작 방식

# 1-2
# ★주요 기능★
# push() : 데이터를 스택에 넣기
# pop()  : 데이터를 스택에서 꺼내기
# 큐(Queue) : eq, dq

# 2. 스택 구조와 프로세스 스택
# 스택 구조는 프로세스 실행 구조의 가장 기본
# 함수 호출 시 프로세스 실행 구조를 스택과 비교해서 이해 필요

# 3. 자료 구조 스택의 장단점
# 장점 
# - 구조가 단순, 구현이 쉽다
# - 데이터 저장/읽기(read) 속도가 빠르다

# 단점
# - 데이터 최대 갯수를 미리 정해야 한다.★★★★★

# - 파이썬의 경우 재귀 함수는 1000번까지만 호출이 가능
# - 저장 공간의 낭비가 발생할 수 있음
# - 미리 최대 갯수만큼 저장 공간을 확보해야 한다
# - 스택은 단순,빠른 성능을 위해 사용하기 때문에
#   보통 배열구조로 활용

# 재귀 함수
# def recursive(data) :
#     if data < 0 :
#         print("ended")
#     else :
#         print(data)
#         recursive(data -1)

#         print("returned", data)

# recursive(4)

# data_stack = list()
# data_stack.append(1)
# data_stack.append(2)
# print(data_stack)

# # data_stack : list형식이라 pop()내장 함수를 가지고 있음
# print(data_stack.pop())

# stack_list = list()

# def push(data) :
#     stack_list.append(data)

# def pop() :
#     data = stack_list[-1] # list의 마지막 인덱스 값을 가져온다.
#     del stack_list[-1]    # 꺼낸 인덱스를 삭제

#     return print(data)

# for index in range(10) :
#     push(index)
    
# pop()

# 백준 5585번 거스름 돈
# num = int(input())
# n = 1000 - num
# num_list = [500, 100, 50, 10, 5, 1]
# count = 0

# print(num_list)

# for i in num_list :
#     count += n // i
#     n %= i

# print(count)


def __init__(self):
        self.list = list()
 
def push(self, data):
        self.list.append(data) # self.list배열에 입력받은 매개변수 data를 추가로 넣는다
 
def pop(self):
        return self.list.pop() # self.list에 있는 배열 중 인덱스 값을 호출 후 delete
 
class Calculator:
    def __init__(self): # __init__(self) : 생성자 / self는 첫번째에 무조건 넣어줘야 한다. / self는 자기자신을 의미(본인 클래스를 의미)
        self.stack = Stack() # LIFO
 
    def calculate(self, string):
        pass
 
# Test code
calc = Calculator()
print(calc.calculate('4 6 * 2 / 2 +'))
print(calc.calculate('2 5 + 3 * 6 - 5 *'))





