# 순차 탐색
# - 탐색은 여러 데이터 중에서 원하는 데이터를 찾아내는 것을 의미
# - 데이터가 담겨있는 리스트를 앞에서부터 하나씩 비교해서 원하는 데이터를 찾는 방법

# random에서 모든 함수를 사용 설정
from random import *
# randint : randint(가져올 데이터의 수, 범위 지정(랜덤))
rand_data_list = list()
for num in range(10):
    # 가져올 데이터 수가 1개이기 때문에 중복을 고려해서 넣지 않는다.
    rand_data_list.append(randint(1, 100))

print(rand_data_list)

def sequencial(data_list, search):
    for index in range(len(data_list)):
        if data_list[index] == search:
            return index
    return -1 # 데이터가 없는 경우

print(sequencial(rand_data_list, 91))

# 시간복잡도
# 최악의 경우 리스트 길이가 n일 때 n번 비교해야 한다
# O(n)
