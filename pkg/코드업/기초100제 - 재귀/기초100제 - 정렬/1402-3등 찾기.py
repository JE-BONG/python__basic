# 배열에 문자열,정수형을 동시에 어떻게 저장할것인가

n = int(input())

for i in range(n):
    data_list = list(map(int, input().split()))
    data_list.sort()
    print(data_list)
    if data_list[2] > data_list[1] and data_list[2] < data_list[3]:
        print(data_list[2])
