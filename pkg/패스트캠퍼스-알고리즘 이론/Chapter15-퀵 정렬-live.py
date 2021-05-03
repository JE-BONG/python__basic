# 퀵 정렬(quick sort)
# - 기준점(pivot)을 정해서, 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 함수
# - 각 왼쪽, 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복
# - 함수는 왼쪽 + 기준점(pivot) + 오른쪽을 리턴

# pivot은 맨처음 데이터로 선정
# 두번째 데이터부터 pivot 기준 분류
def qsort(list):
    pivot = list[0]
    for n in range(1, len(list)):
        if pivot > list[n] : 
            left.append(list[n])
        else :
            right.append(list[n])

# 데이터 1개일 때 (recursive call 적용)
# 두번째 데이터부터 pivot 기준 분류
def qsort(list):
    if len(list) <= 1: 
        return list
    pivot = list[0]
    for n in range(1, len(list)):
        if pivot > list[n]:
            left.append(list[n])
        else:
            right.append(list[n])
    return qsort(left) + [pivot] + qsort(right) # recursive call 적용

def qsort(data):
    if len(data) <= 1:
        return data
    left, right = list(), list() # left,right에 정렬해서 담을 list 생성
    pivot = data[0]
    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
    # [pivot] : list로 만들어 정렬하기 위함
    # 위 for문 모두 끝나면 다시 재귀로 아래 정렬된 리스트를 qsort로 호출 후
    # pivot = 맨앞 인덱스는 또 바뀌어 있다.
    # 그리고 또 for문을 통해 정렬 실행한다.
    return qsort(left) + [pivot] + qsort(right)

import random
data_list = random.sample(range(100), 10)
# print(data_list)
# print(qsort(data_list))

def qsort1(data):
    if len(data) <= 1:
        return data
    pivot = data[0]

    # for문을 통해 슬라이싱으로 인덱스1번부터 item에 입력하는데
    # pivot보다 작은 item만 item에 삽입된다.
    left = [item for item in data[1:] if pivot > item]
    right= [item for item in data[1:] if pivot <= item]

    return qsort(left) + [pivot] + qsort(right)

import random
data_list = random.sample(range(100), 10) # 0 ~ 99까지 10개의 랜덤숫자 list형태로 저장 
print(data_list)
print(qsort1(data_list))




















