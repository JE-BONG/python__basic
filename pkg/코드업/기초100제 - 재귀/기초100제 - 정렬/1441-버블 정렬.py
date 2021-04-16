# def data(data_list):
#     while data_list:
#         if len(data_list) == data_list.index(len(data_list)-1):
#             return True

n = int(input())
data_list = list(0 for i in range(n))
for i in range(n):
    data_list[i] = int(input())

for i in range(len(data_list)-1):
    for j in range(len(data_list)-1):
       if data_list[j] > data_list[j+1]:
            data_list[j],data_list[j+1] = data_list[j+1],data_list[j]

print(data_list)

# 구구단 만들기
# n = int(input('1~9단 까지 구구단을 출력하세요.'))
# data_list = list(i * 1 for i in range(n+1))
# del data_list[0]

# for i in data_list:
#     print('--------------------------------------')
#     print(i, '단')
#     print('--------------------------------------')
#     for j in data_list:
#         print(i,'x', j, '=', i * j)