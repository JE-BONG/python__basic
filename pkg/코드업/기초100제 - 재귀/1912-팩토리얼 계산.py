# 방법1
n = int(input())

def sum_list(n):
    if n == 1:
        return n
    return n * sum_list(n-1)

print(sum_list(n))