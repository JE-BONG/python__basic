n = int(input())

data_list = list(map(int, input().split()))

for index in range(len(data_list)-1): # 0 ~ 4
    for index2 in range(len(data_list)- index -1):
        if data_list[index2] < data_list[index2+1]:
           data_list[index2],data_list[index2+1] = data_list[index2],data_list[index2+1]
        else:
           data_list[index2],data_list[index2+1] = data_list[index2+1],data_list[index2]
        

print(data_list)