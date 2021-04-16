n = int(input())
data_list = list(i*1 for i in range(n))

for i in range(len(data_list)):
    data_list[i] = int(input())

data_list.sort()
print('=======================================')

for j in range(len(data_list)):
    print(data_list[j])
