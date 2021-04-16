# 대표적인 정렬3: 선택 정렬(selection sort)

# 1. 선택 정렬
# - 다음과 같은 순서를 반복하여 정렬하는 알고리즘
# 1) 주어진 데이터 중, ★최소값★을 찾음
# 2) 해당 최소값을 데이터 맨 앞에 위치한 값과 교체
# 3) 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복
# 참고 : https://visualgo.net/en/sorting
# 참고 : https://en.wikipedia.org/wiki/Selection_sort

# 2. 코드 방법
# 1) 데이터가 2개 인 경우
# ex: dataList = [9, 1]
#     dataList[0] > dataList[1] : datalist[0], dataList[1] 이 서로 값을 교환

# 2) 데이터가 3개 인 경우
# ex: dataList = [9, 1, 7]
#     처음 실행 시 1, 9, 7
#     두번 실행 시 1, 7, 9

# 3) 데이터가 4개 인 경우
# ex: dataList = [9, 3, 2, 1]
#     처음 실행 시 1, 3, 2, 9
#     두번 실행 시 1, 2, 3, 9
#     세번 실행 시 변화 없음

# 3. 알고리즘 구현
def selection_sort(data):
    for stand in range(len(data)-1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest],data[stand] = data[stand],data[lowest]
    return data

import random
# range를 통해 list로 만들어준다.
data_list = random.sample(range(100), 10)
print(selection_sort(data_list))