# 방법 1
n = int(input())
def num(n):
     if n == 1:
         return 1
     else:
         return n + num(n-1)
print(num(n))
    
# 방법 2
n = int(input())
def total(n):
     if n != 1 :
         print(n)
         return n + total(n - 1)
     else :
         return 1
print(total(n))




