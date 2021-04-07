print('hello')
# 8393번
# sum = 0
# inp = int(input())
# for i in range(inp+1):
#     sum = sum+i
#     print(sum)

# 15552번 (빠른 A+B)

# num = int(input())

# for i in range(num) :
#     a,b = map(int, input().split())
# print(a+b)

# 1000번
# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a + b)
# print(a - b)
# print(a * b)
# print(int(a / b))
# print(a % b)

# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# print((a+b)%c)
# print((a%c + b%c)%c)
# print((a*b)%c)
# print((a%c)*(b%c)%c)

# 전체 주석 : ctrl + /

# while True :
#     a, b = map(int, input().split())
#     if a == 0 and b == 0 :
#         print('반복 종료')
#         break
#     else :
#         print(a+b)

# ★input().split() 결과 : 문자열 반환★
# a, b, c = map(int, input().split())
# a = a
# b = b
# c = c
# total = list(str(a * b * c)) # total은 결과를 가지고 있다.
# print(total)
# for i in range(len(total)+2) :
#     print(total.count(str(i)))

# # 10818 번 문제
# data = int(input())
# n = list(map(int, input().split()))

# print(min(n), max(n))

# # len : 배열, 리스트, 튜플, 딕셔너리, set 등 배열의 길이를 반환

# # 2562번 문제
# 1~9 까지
# data.index()
# data = []
# for i in range(9) :
#     data.append(int(input()))
# print(max(data))
# print(data.index(max(data))+1)
# index : 찾으려는 값의 인덱스 번호를 알려준다.
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# print(data)
# first = max(data)  # 슬라이싱으로 마지막 인덱스인 -1에 있는 값이 최고값
# second = max(data) - 1

# result = 0

# while True : 
#     for i in range(k) : # 0 ~ 2 = 3 / 0 1 2 3
#         if m == 0 :
#             break       # 같다면 반복문 탈출
#         result += first # + 6 + 6 + 6 + 6
#         m -= 1 # 7 5 3 2
#     if m == 0 :
#         break
#     result += second # + 5 + 5 + 5 + 5
#     m -= 1 # 6 4 2 1

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n - 1]
# second = data[n - 2]

# count = int(m / (k+1)) * k  # 6
# count += m % (k+1)          # 0

# result = 0
# result += (count) * first   # 36
# result += (m - count) * second # 10
# print(result)

# print(result)

# count = int(m / (k+1)) * k
# count += m % (k + 1)

# result = 0
# result += (count) * first
# result += (m - count) * second

# ----------------------------------------------------------------------
# print(result)
# 백준 5585번 (Greedy 문제)
# num = int(input()) 
# n = 1000 - num # 620원
# count = 0

# coin_types = [500, 100, 50, 10, 5, 1] # 가게가 가지고 있는 돈

# for coin in coin_types: # 총 6번 반복
#     count += n // coin  # 1, 1, 0, 2, 0, 0
#     n %= coin           # 120, 20, 0, 0, 0, 0

# print(count)
# print(n)
# -----------------------------------------------------------------------------

# CodeUp 3301 : 거스름 돈
# num = int(input())
# num_list = [50000, 10000, 5000, 500, 100, 50, 10]  
# count = 0

# while num >= 0 :
#      for i in num_list :
#              num -= i # - 50000   
#              print(num)
#              count += 1
# print(count)

# num = int(input())

# count = 0
# money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

# for m in money :
#      count += num//m # money에서 나눈 값이 카운트로 올라간다.
#      num = num%m     # 입력받은 값에서 money를 순차적으로 나눈 후 몫이 들어간다.

# print(count)
# ---------------------------------------------------------------------
# n, m = map(int, input().split()) # n , m 변수에 각 값 입력

# result = 0
# for i in range(n): # 0 ~ 2 : 총 3번 실행
#     data = list(map(int, input().split())) # list(순서/중복o // 수정,삭제 가능) 형식으로 무제한으로 수를 받는다
#     min_value = min(data)                  # min_value 변수에 min(데이터)를 통해 가장 작은 수 저장
#     # max : result와 min_value에 있는 값 중 큰 수를 반환
#     result = max(result, min_value)        # result에 있는 현재 값과, min_value에 있는 값 중 큰 수를 반환
# print(result)

#----------------------------------------------------------------------
# 10162번 : 전자레인지
# 최소횟수가 답으로 인정
# A = 5분(300초)
# B = 1분(60초)
# C = 10초
# T = int(input()) # 요리시간(정수)
# num_list = list(map(int, input().split())) # 300, 60, 10 

# for i in num_list:
#     # i가 T보다 크면 입력값을 맞출 수 없기 때문에 break
#     if i > T :
#         print('STOP')
#         break
    
# T = int(input())

# if T % 10 != 0:
#     print(-1)
# else:
#     A = B = C = 0
#     A = T // 300
#     print(A) # 0

#     B = (T % 300) // 60 # 1
#     print(B)
    
#     C = (T % 300) % 60 // 10  # 4
#     print(C)

#     print( T % 300 ) # 100으로 300을 나눌 수 없기에 100 유지
#     print(A, B, C)    
# ----------------------------------------------------------------------
# 1이 될때까지(Greedy)
# N, K = map(int, input().split())
# count = 0

# # 참일 경우 수행
# while N >= K :         # 두번 째엔 수행이 안된다(한번 수행 후 N이 4로 변경되었기 때문 그 아래 WHILE문도 자동 실행안됨)
#     while N % K != 0 : # 0과 같으면 종료 # 1번째부터 실행 안됨 나머지값이 0이라서 조건 성립안됨
#             N -= 1     # 건너뛰기
#             count += 1 # 건너뛰기
#     N //= K # 25/5 = 5
#     print(N)
#     count += 1 # 1

# while N > 1: # 5(n) > 1
#     N -= 1   # 4(N)
#     count+=1 # count : 2

# print(count)
# ---------------------------------------------------------------------

# 1.
# n = int(input()) # 배달할 킬로그램
# count = 0 

# if n < 3 or n > 5000 :
#      n = 0
#      print(n ,'의 값이 초과되거나 미달입니다.')
#      count = 0        # 봉지 개수

# while n >= 0 :
#      if n % 5 == 0 : # n의 정수로 나누어지는 경우 실행
#         count += (n // 5) 
#         break

#      n -= 3
#      count += 1
# else : # n의 정수로 나누어지지 않는 경우 실행
#     n -= 3
#     count += 1
# print(count)

# 2. 
# sugar = int(input())

# bag = 0
# while sugar >= 0:       # 입력받은 값이 0보다 클 경우 아래 내용 실행
#     if sugar % 5 == 0 : # 18에서 5를 나누고 난 나머지값이 0과 같다면 
#         bag += (sugar // 5) # bag에는 3을 더한다
#         print(bag)
#         break
    
#     # break위에 조건이 성립이 안되면
#     sugar -= 3 # sugar에서 -3씩 계속 감소
#     bag += 1   # 0이 될 때까지 카운트는 계속 올라간다.

# else : # sugar이 0보다 작거나 같을 경우 출력
#     print(-1)
# ------------------------------------------------------------------------
# 백준 2839 : 설탕배달 for문 활용
# n = int(input())
# num_list = list(map(int, input().split()))

# count = 0
# for i in num_list :
#     count += n // i
#     n = n%i

# print(count)
# ------------------------------------------------------------------------
# 백준 2217 : 로프
# N = list(map(int, input().split()))
# print(N)
# k = 0
# for i in N :
#     k += int(i)

# print(int(k / 3))


# while w != 0 :

# 로프끼리의 힘을 통해 동일하게 배분하여 중량을 올려야 하기 때문에 한로프에만 모두 줄 수 없다
# 15kg는 10로프가 못올려서 안되고
# 10kg는 15로프도 10로프도 10씩 배분하여 올릴 수 있기 때문에 각 10씩하면 총 20이 max값이다.
# def solution():
#     answer = 0
#     arr.sort(reverse=True)
#     for i in range(N): # 0, 1
#         # 15 * 0+1 = 15 / 10 * 1+1 = 20(최대중량)
#         arr[i] = arr[i] * (i + 1)
 
#     return max(arr)
 
# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(int(input()))
 
# print(solution())

data = list(map(int, input().split()))

data.sort()

print(data[0], data[1], data[2])

    
    
    
    





























































        




























