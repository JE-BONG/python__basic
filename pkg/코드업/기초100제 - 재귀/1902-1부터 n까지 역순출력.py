# 방법1.
n = int(input())

def rever(n): # 10
    if n == 0:
        return  
    print(n)
    return rever(n - 1)

rever(n)