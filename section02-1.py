# Section02-1
# 파이썬 기초 코딩
# 참조 : https://www.python.course.eu/python3_formatted_output.php
# Print 구문의 이해
# 큰 따옴표 / 작은 따옴표 가능

# 기본 출력
print('Hello Python!')
print("Hello Python!")
print('''Hello Python!''')
print("""Hello Python!""")

print()

# Separator 옵션 사용
# <sep>
# sep : 작은따옴표에 있는 공백을 붙여준다
print('T','E','S','T',sep='\t')
# 사이에 - 를 붙여서 출력해준다
print('2019', '02', '19', sep='-')
# @를 중간에 붙여서 출력해준다
print('niceman','google.com', sep='@')

# <end> 옵션 사용
# end : 끝 부분을 다음 문장과 붙여서 출력해준다 
# java로 설명하면 \n이 없는 상태
print('Welcome To', end='\t')
print(' the black parade', end='\t')
print('piano notes')

print()

# <format> 사용
# ex : format(문구1, 문구2)
# ex : format(a='문구1', b=1)
# [] : 대괄호 / {} : 중괄호 / () : 소괄호
print('{} and {}'.format('You', 'Me'))
# 인덱스 0번 : you / 1번 : Me
print("{0} and {1} and {0}".format('You','Me')) 
print("{a} are {b}".format(a='You', b='Me'))

# format 사용 없이 사용할 경우
# %를 사용해 format 대신 사용
#%s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" %('jebong',7)) 

# %5d : 5자까지 정수형 가능 / %4.2f : 실수 4자리와 소수점2자리까지만 출력
print("Tset1: %5d, price: %4.2f" %(776, 6534.123))
# 인덱스 0번 / 인덱스 1번 사용 시 
print('Test1: {0: 5d}, price: {1: 4.2f}'.format(776, 6534.123)) 
print('Test1: {a: 5d}, price: {b: 4.3f}'.format(a=776, b=6534.123))

print("'you'") # 큰 따옴표 안에선 작은 따옴표가 출력된다 / 반대는 안됨
# \를 통해 구분 짓는다?
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\t\t\ttest')
