# # 방법 1
# n = int(input())
# def num(n):
#      if n == 1:
#          return 1
#      else:
#          return n + num(n-1)
# print(num(n))
    
# # 방법 2
# n = int(input())
# def total(n):
#      if n != 1 :
#          print(n)
#          return n + total(n - 1)
#      else :
#          return 1
# print(total(n))

# # 방법 3
data = int(input())
num = 0

def sum_list(num):
    if num == data:
        return num
    return num + sum_list(num+1)
    

print(sum_list(num))




