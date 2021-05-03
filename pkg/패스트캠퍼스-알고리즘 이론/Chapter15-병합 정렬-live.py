# <병합 정렬>
# 참고 : https://visualgo.net/en/sorting 

# 데이터가 4개인 경우
# data = [1, 9, 3, 2]
# 1. 먼저 [1, 9], [3, 2]로 나눈다
# 2. 다시 앞 부분 [1],[9]로 나눈다
# 3. 다시 정렬해서 합친다 [1, 9]
# 4. 다음 [3, 2]는 [3][2]로 나누고
# 5. 다시 정렬해서 합친다 [2, 3]
# 6. 이제 [1, 9], [2, 3]을 합친다.
# - 1 < 2 이니 [1]
# - 9 > 2 이니 [1, 2]
# - 9 > 3 이니 [1, 2, 3]
# - 9 밖에 없으니 [1, 2, 3, 9]
# import random

# def split(data):
#     medium = int(len(data) / 2)
#     left = data[:medium]  # 0 ~ 2까지중 마지막 인덱스인 2의 앞숫자인1까지 출력
#     right = data[medium:] # 2번인덱스를 포함한 ~ 마지막 인덱스까지 출력
#     print(left, right)

# data_list = [3,4,1,3]
# split(data_list)

def mergesplit(data):
    if len(data) <= 1 :
        return data
    medium = int(len(data) / 2)
    # 마지막 data 길이가 1이 될 때까지 쪼갠다
    left = mergesplit(data[:medium]) # 0번인덱스부터 medium의 전 인덱스까지
    right = mergesplit(data[medium:])# medium인덱스부터 마지막 인덱스까지
    return merge(left, right)

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0 # 각 리스트 인덱스0번

    # case1 : left / right가 아직 남아있을 때
    # left_point는 비교할 때마다 바뀐다
    # - left나 right중 둘 중 하나가 배열길이보다 더 크거나
    # - 둘 다 배열길이랑 같거나 클 경우 while문 종료
    # 즉, 아직 비교할 배열의 데이터가 남아있는 경우를 의미
    while len(left) > left_point and len(right) > right_point:
        # 각 left, right 처음 인덱스끼리 비교
        if left[left_point] > right[right_point]:
            # 미리 만들어 놓은 meged리스트뒤에 append를 통해 
            # right[right_point]값을 넣는다.
            merged.append(right[right_point])
            # 그리고 다시 left[left_point]와 새로운 right[right_point]의 
            # 비교를 위해 +1을 해준다.
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 : left만 남아있을 때
    # 위 while문 조건식이 성립이 되지 않을 경우 실행
    # left와 right비교 후 right가 더 이상 존재하지 않을 경우
    # 나머지 left에 남아있던 배열값들을 append를 통해 
    # meged리스트에 차례대로 넣는다.
    while len(left) > left_point:
        merged.append(left[left_point])
        # point를 1씩 늘려 1개씩 차례대로 넣는다.
        left_point += 1

    # case3 : right만 남아있을 때
    # 위 설명과 동일
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

import random
data_list = random.sample(range(100), 10)
print(mergesplit(data_list))
# 슬라이싱은 [:번호] = 번호가 아닌 번호앞 인덱스까지를 의미 

# 시간복잡도
# ex)
# 몇 단계 깊이까지 만들어지는지를 depth 라고 하고 i로 놓는다. 맨 위 단계는 0으로 놓는다.
# 단계는 항상 log2n개 만큼 만들어진다 
# 시간 복잡도는 결국 O(log n), 2는 역시 상수이므로 삭제
# 따라서, 단계별 시간 복잡도는 O(n) * O(log n) = O(n log n) 이다.


























    