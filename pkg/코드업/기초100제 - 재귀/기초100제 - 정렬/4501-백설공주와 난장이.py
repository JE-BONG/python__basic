n = int(input())
num1 = 0
num2 = 0
data_list = list(i * 1 for i in range(n))
for s in range(n):
     data_list[s] = int(input())

print(data_list)
for i in range(len(data_list)-1):
    for j in range(len(data_list)-1):
        if data_list[j] > data_list[j+1]:
            data_list[j],data_list[j+1] = data_list[j+1],data_list[j]

print(data_list)
print(max(data_list))
print(data_list[len(data_list)-2])
