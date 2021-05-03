# n = int(input())

# def starsum(n):
#     s = '*'
#     if n == 1:
#         return s
#     return starsum(n-1) + '\n' + s * n

# print(starsum(n))


# 4564 - 계단오르기
n = int(input()) # 계단의 개수
data_list = list(i * 1 for i in range(n))
for i in range(n):
    data_list[i] = int(input())

for j in range(len(data_list)):
    # 전체 배열길이에서 3나누기나 나머지를 통해 3의 배열일 때 continue로 건너뛴다.
    # 연속된 세개의 계단을 밟을 수 없고, 두 계단씩 오르기 위함
    if data_list[j] % 3 == 3 :
        continue

print(data_list)