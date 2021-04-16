import random

# n = int(input())
# num = list([i*1 for i in range(n)])
# for i in range(n):
#     num[i] = random.randint(0, 9)

# num.sort(reverse=True)
# print(num)

n = int(input())
num = list([i*1 for i in range(n)])
for i in range(n):
    num[i] = random.randint(0, 9)

my_set = set(num)
my_list = list(my_set)
print(my_list)