# 예를 들어, 10 50 30 20 40 이 있고 오름차순으로 정렬한다면 총 4단계를 거치게되는데,

# 1단계 : 10 30 20 40 50

# 2단계 : 10 20 30 40 50  (정렬 완료)

# 3단계 : 10 20 30 40 50

# 4단계 : 10 20 30 40 50

# 4단계중 이미 2단계에서 정렬이 완료가 된다.
# 이 단계를 구하는것이 문제이다. 이 단계를 찾아 프로그램을 종료시키면 정렬속도를 향상 시킬수있다.
# 이 단계를 찾아 내는 프로그램을 작성하시오.
n = int(input())
num = list(i * 1 for i in range(n))
count = 1

for i in range(n):
    num[i] = int(input())

for index in range(len(num)-1):
    for index2 in range(len(num)+1):
        if num[index] > num[index2]:
            count += 1
            num[index],num[index2] = num[index2],num[index]
        else:   
            break

print(count)


