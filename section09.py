# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : read 
# 쓰기 모드(기존 파일 삭제) : write
# 추가 모드(파일 생성 또는 추가) : append
# ..   : 상대 경로
#  .   : 절대 경로
# 참고 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기 : read
# 예제1
# open(파일 경로 작성)
# f = open('C:/work/python_basic/.vscode/resource/review.txt', 'r')
# content = f.read()
# print(content)
# print(dir(f))
# 반드시 close 리소스 반환해야 한다★
# f.close()

# 예제2
# with : close() 생략 가능
# read : 파일 읽어들이기
print('<예제2>')
print('read : 파일 읽어들이기')
print()
with open('C:/work/python_basic/.vscode/resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c)) # 형 변환(char)
    print(iter(c)) # iterator 반환

print()
print('--------------------------------------------------------')

# 예제3
print('<예제3>')
print('strip() : 양쪽 공백 제거')
print()
with open('C:/work/python_basic/.vscode/resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) 
        # strip() : 양쪽 공백 제거
    
print()
print('--------------------------------------------------------')

# 예제4
print('<예제4>')
print('동일한 내용 출력되지 않는 내용')
print()
with open('C:/work/python_basic/.vscode/resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    # 위에서 동일한 내용을 읽고 커서가 끝으로 가있기 때문에 
    # 아래 내용은 출력 되지 않는다.
    content = f.read() 
    print(">", content) 

print()
print('----------------------------------------------------------')

# 예제5
# readline() : 문장의 한줄씩 읽어오기 / 커서는 맨 끝에 위치해 있다. (읽어들일 준비 완료)
print('<예제5>')
print('readline() : 각 문장의 한줄씩 read')
print()
with open('C:/work/python_basic/.vscode/resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    # true : 1 
    # false: 0
    while line :             # line에 내용이 있다면 (내용이 없을 때 까지 읽어온다.)
        print(line, end='#### ',) 
        line = f.readline()  # 한줄 씩 읽어오기(line에 있는 다음문장을 읽어온다.)

print()
print('----------------------------------------------------------')

# 예제6
print('<예제6>')
print('readlines : 모든 문장을 엔터를 기준으로 줄바꿈 기준을 list()형태로 가지고 있다. ')
with open('C:/work/python_basic/.vscode/resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    # list형태로 출력되기 때문에 for문 가능
    for c in contents :
        print(c, end = '***** ')

print()
print('----------------------------------------------------------')

# 예제7
print('<예제7>')
score = []
with open('C:/work/python_basic/.vscode/resource/score.txt', 'r') as f:
    for line in f:
        # text파일은 문자열로 인식되기 때문에 형변환 필수
        score.append(int(line)) 
    print(score)
    
print('Average :  {:6.3}'.format(sum(score)/len(score)))
print()
print('----------------------------------------------------------')

# 파일 쓰기
print('<파일 쓰기>')
print('예제1')
with open('C:/work/python_basic/.vscode/resource/review.txt', 'w') as f:
    f.write('Niceman\n')

print('예제2')
with open('C:/work/python_basic/.vscode/resource/review.txt', 'a') as f:
    f.write('Goodman\n')

print()
print('예제3')
from random import randint
with open('C:/work/python_basic/.vscode/resource/review2.txt', 'w') as f:
    for cnt in range(6) : # 0 ~ 5 6번 반복
        f.write(str(randint(1, 50)))
        f.write('\n')

print()
print('-------------------------------------------------------------')
# 예제4
# writelines : list -> 파일로 저장하는 형태
# list로 된 파일을 쓰는 예제
print('예제4')
with open('C:/work/python_basic/.vscode/resource/review2.txt', 'w') as f:
    list = ['kim', 'park\n', 'cho\n']
    f.writelines(list)

print()
print('-------------------------------------------------------------')
# 예제5
print('예제5')
print('print : 콘솔이 아닌 파일로 저장된다.')
with open('C:/work/python_basic/.vscode/resource/review2.txt', 'w') as f:
    print('Test Contest1!', file=f)
    print('Test Contest12', file=f)
















