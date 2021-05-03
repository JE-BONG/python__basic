n = int(input())

data_list = list(i for i in range(n)) # 0, 1, 2, 3, 4

for i in range(len(data_list)):
    data_list[i] = list(map(int, input().split()))

print(data_list[0][1])

for i in range(len(data_list)-1):
    for j in range(len(data_list)-1):
        # 1. 수학 점수가 높은순으로 정렬
        if data_list[j] > data_list[j+1]:
            data_list[j],data_list[j+1] = data_list[j],data_list[j+1]
            if data_list[j][j+1] > data_list[j+1][j+1]:
        # 2. 수학 점수가 같으면 정보 점수가 높은순으로 출력
        # if data_list[j] == data_list[j+1]:
        #     if data_list[j][j] < data_list[j+1][j+1]:
        #         data_list[j][j],data_list[j+1][j+1] = data_list[j+1][j+1],data_list[j][j]
        
for i in range(len(data_list)):
    print(i, data_list[i]) 
            