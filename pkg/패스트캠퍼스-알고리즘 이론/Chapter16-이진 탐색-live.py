# 이진 탐색(Binary Search)
# - 탐색할 자료를 둘로 나누어 해당 데이터가 있을만한 곳을 탐색하는 방법

# 이진탐색과 순차탐색의 차이
# - www.mathwarehouse.com

# 분할 정복과 이진탐색의 차이
# <분할 정복>
# Divide : 문제를 하나 또는 둘 이상으로 나눈다
# Conquer: 나눠진 문제가 충분히 작고, 해결이 가능하면 해결, 아니면 다시 나눈다.
# <이진 탐색>
# Divide : 리스트를 두 개의 서브 리스트로 나눈다.
# Conquer
# - 검색할 숫자 > 중간값 이면, 뒷 부분의 서브 리스트에서 검색할 숫자를 찾는다.
# - 검색할 숫자 < 중간값 이면, 앞 부분의 서브 리스트에서 검색할 숫자를 찾는다.

def binary_search(data, search):
    print(data)
    # 반으로 쭉 나누다가 데이터리스트의 길이가 1이고 
    # 검색할 search가 남은 data[0]값과 동일하다면
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False
    
    medium = len(data) // 2 # 몫을 출력
    # 전체 data리스트에서 medium의 인덱스 값을 출력 시 search와 동일하면 True
    if search == data[medium]:
        return True
    else:
        # search값이 data[medium]보다 크다면
        # 최소 앞이 아닌 뒤에있다
        if search > data[medium]:
            # return 시 data[medium:]을 통해 슬라이싱으로 medium이 있는
            # 인덱스값부터 끝까지 다시 재귀호출을 통해 보낸다.
            return binary_search(data[medium:], search)
        else:
            return binary_search(data[:medium], search)

import random
data_list = random.sample(range(100), 10)
data_list.sort()
print(data_list)
print(binary_search(data_list, 91))