# 동적 계획법 and 분할 정복

# <동적 계획법>(DP)
# 입력 크기가 작은 부분 문제들을 해결한 후, 해당 부분 문제의 해를 활용해서, 보다 큰 크기의
# 부분 문제를 해결, 최종적으로 전체 문제를 해결하는 알고리즘
# 상향식 접근법, 최하위 답을 구한 후, 저장 후, 해당 결과값을 통해 상위 문제를 풀어가는 방식

# Memoization 기법 사용
# Memoization : 프로그램 실행 시, 이전에 계산한 값을 저장 후 다시 계산하지 않도록 하여 전체 실행
#               속도를 상향
# 문제를 잘게 쪼갤 때, 부분 문제는 중복되어, 재활용 된다
# 예 : 피보나치 수열

# <분할 정복>
# 문제를 나눌 수 없을 때까지 나누어서 각가을 풀면서 다시 합병하여 문제의 답을 얻는 알고리즘
# 하향식 접근법으로 상위의 해답을 구하기 위해, 아래로 내려가면서 하위의 해답을 구하는 방식
# 예 : 재귀함수
# 문제를 잘게 쪼갤 때, 부분 문제는 서로 중복되지 않는다.
# 예 : 병합 정렬, 퀵 정렬 등

# <공통점>
# - 문제를 잘게 쪼개, 가장 작은 단위로 분할

# <차이점>
# 1. 동적 계획법
# - 부분 문제는 중복, 상위 문제 해결 시 재활용 된다
# - Memoization 기법 사용 (부분 문제의 해답을 저장 후, 재활용 하는 최적화 기법)
# 2. 분할 정복
# - 부분 문제는 서로 중복되지 않는다
# - Memoization 기법 사용x

# 재귀용법 활용
def fibo(num):
    if num <= 1: 
        return num
    return fibo(num -1) + fibo(num -2)

print(fibo(4))

print(fibo(3) + fibo(2))

# 동적 계획법 활용(DP)
def fibo_dp(num):
    # 참고:https://www.fun-coding.org/PL&OOP5-2.html
    # list형식의 배열이 만들어진다 인덱스 0번부터~
    cache = [0 for index in range(num + 1)] 
    cache[0] = 0
    cache[1] = 1
    # 피보나치 수열 구하는 방식
    for index in range(2, num+1):
        # cache[index] = cache[1] + cache[-2] 의 값이 더해진다
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[num]
print(fibo(10))


