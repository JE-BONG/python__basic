# 상하좌우

n = int(input()) # 5
x, y = 1, 1
plans = input().split()

# 동 서 북 남
dx = [0, 0, -1, 1] # 행
dy = [-1, 1, 0, 0] # 열
move_types = ['L','R','U','D']

# 이중 for문
for plan in plans: # R R R U D D 차례로 입력
     for i in range(len(move_types)):
         if plan == move_types[i]: # R R R U D D(한 단어당 4번 반복)
             nx = x + dx[i] 
             print('nx의 현재 값:', nx) 
             ny = y + dy[i] 
             print('ny의 현재 값:', ny)
             print('------------------------------------------')
     if nx < 1 or ny < 1 or nx > n or ny > n:
         continue # 해당되는 내용이 있으면
                  # 아래 x, y = nx, ny대입하는건 건너뛴다.
     x, y = nx, ny
     print('기존x값 :', x)

print(x, y)
