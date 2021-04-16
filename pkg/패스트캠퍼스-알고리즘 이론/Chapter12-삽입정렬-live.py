# 1. 삽입 정렬 (insertion sort)
# - 삽입 정렬은 ★두 번째 인덱스★부터 시작
# - 해당 인덱스(key 값) 앞에 있는 데이터(B)부터 비교해서 
#   key 값이 더 작으면 B값을 뒤 인덱스로 복사
# - 이를 key 값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치
#   바로 뒤에 key 값을 이동
# 참고 : https://visualgo.net/en/sorting
# 이해 : https://goo.gl/XKBXuk

# 2. 알고리즘 구현
def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2],data[index2 -1] = data[index2 - 1],data[index2]
            else:
                break
    return data
import random

data_list = random.sample(range(100), 10)
print(insertion_sort(data_list))

# 2-1
rand_data_list = [3, 5, 1, 2]
def insertion_sort2(data_list):
    for stand in range(len(data_list)-1):
        key = data_list[stand] # 0번째 인덱스의 value 포함
        for num in range(stand, 0, -1):
            if key < data_list[num - 1]:
                data_list[num-1], data_list[num]
            else:
                break
    return data_list

print(insertion_sort2(rand_data_list))


# 3. 알고리즘 분석
# - 버블정렬과 동일하다.