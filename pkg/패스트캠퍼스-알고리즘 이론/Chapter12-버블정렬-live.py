# 알고리즘 연습 방법
# 1. 연습장과 펜을 준비
# 2. 알고리즘 문제를 읽고 분석 후
# 3. 간단하게 테스트용으로 매우 간단한 경우부터 복잡한 경우 순서대로 생각해보면서,
#    연습장과 펜을 이용하여 알고리즘을 생각한다.
# 4. 가능한 알고리즘이 보인다면, 구현할 알고리즘을 세부 항목으로 나누고, 문장으로
#    세부 항목을 나누어서 적는다
# 5. 코드화하기 위해, 데이터 구조 또는 사용할 변수를 정리
# 6. 각 문장을 코드 레벨로 지정한다.
# 7. 데이터 구조 또는 사용할 변수가 코드에 따라 어떻게 변하는지를 손으로 적으면서,
#    임의 데이터로 코드가 정상 동작하는지를 연습장과 펜으로 검증한다.

# 대표적인 정렬1 : 버블 정렬(bubble sort)

# 1. 정렬(sort) 이란
# - 정렬(sorting) : 어떤 데이터들이 주어졌을 때, 이를 정해진 순서대로 나열하는 것
# - 정렬은 프로그램 작성 시 빈번하게 필요로 함
# - 다양한 알고리즘이 고민되었으며, 알고리즘 학습의 필수

# 다양한 정렬 알고리즘 이해를 통해, 동일한 문제에 대해 다양한 알고리즘이 고안될 수 있음을
# 이해하고, 각 알고리즘간 성능 비교를 통해, 알고리즘 성능 분석에 대해 이해

# 2. 버블 정렬(bubble sort) 이란
# - 두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘
# 참고 : https://visualgo.net/en/sorting

# 정렬 연습

# for index in range(num-1):
#     if num[index] > num[index+1]:
#         num[index],num[index+1] = num[index+1],num[index]
#         print(num)
# ---------------------------------------------------------------------------

def bubblesort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2+1]:
                data[index2],data[index2+1] = data[index2+1],data[index2]
                swap = True
        if swap == False:
            break
    return data
    
import random
# random.sample : list() 형식으로 0 ~ 99개 중 50개를 랜덤으로 넣는다.
for index in range(3):
    data_list = random.sample(range(100), 50)
    print(bubblesort(data_list))

# ---------------------------------------------------------------------------

# 2개 일 때
# 3개 일 때
# 4개 일 때

# for num in range(data_list) 반복
# swap = False로 상태 확인
# 외부 for문 안에서 내부 for문을 통해 
# for index in range(len(data_list) - num - 1):
#   if data_list[index] > data_list[index+1]:
#       data_list[index],data_list[index+1] = data_list[index+1],data_list[index]
#       swap = True
#   if swap == False : 
#      break 
#   정렬이 되어 있다는 의미로 for문 종료

# 5. 알고리즘 분석
# 1) 반복문이 두개 이므로 O(n2)
# 2) 완전 정렬이 된 경우 : O(n)

