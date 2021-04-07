# section04-2 
# 문자열, 문자열연산, 슬라이싱★
#====================================================
str1 = "I am boy"
str2 = 'Nice man'
str3 = " "
str4 = str('ace') # 형변환을 통해 넣는다

# 문자열 길이 : len(공백도 길이 추가)
# 자바 : length / 컬렉션 : size()
print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\"" # \역슬래시를 통해 문장에서 탈출 후 ""도 같이 출력된다.
print(escape_str1)
escape_str2 = "Tab \t Tab\t Tab"
print(escape_str2)
#====================================================
# Raw String(있는 그대로 출력)
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)
#====================================================
# 멀티 라인
# \ : 다음 줄과 이어진다고 이해하면 된다 없으면 컴파일 에러
multi = \
"""\n
문자열\n 
멀티라인\n 
테스트\n
"""
print(multi)

#====================================================
# 문자열 연산 
# 공백도 한글자로 포함
str_o1 = '*'
str_o2 = 'abc '
str_o3 = 'd e f'
str_o4 = "Niceman"
print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * len(str_o4))
# in : 'a'라는 글자가 str_o4에 포함되어 있는지 여부 확인
#    : True or False 로 출력
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)
#====================================================
# 문자열 형 변환
# 눈에 보기에는 정수,실수 이지만 결과는 String 이다
print('<문자열 형 변환>')
print(str(77) + 'a')      # '77' + 'a'
print(str(10.4) + 'Good') # '10.4' + 'Good'

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'

#print(a.islower())     # a가 전부 소문자 인지 : false(0)
#print(a.endswith('s')) # 끝 글자가 s로 끝나는지
#print(a.capitalize())  # 첫글자만 대문자로 변환
#print(a.replace('nice', 'good')) # nice를 good으로 변환
#print(list(reversed(b))) # list형태로 b에 담겨있는 오렌지를 거꾸로 반환

#====================================================
# 문자열 슬라이싱★
a = 'niceman'
b = 'orange'
print(a[0:3])     # 0부터 2까지 나온다 3전까지
print(a[0:4])     # nice까지 출력
print(a[0:len(a)])# 인덱스 0부터 a의 길이만큼 출력
print(a[:4])      # 앞은 처음부터 0이라고 인식
print(a[:])       # 처음부터 끝까지 출력
print(b[0:4:2])   # 0부터 3까지 나오되, 2번씩 건너뛰고 나온다(ge제외)
print(b[1:-2])    # 역순으로도 표시
print(b[::-1])    # 처음부터 끝까지 출력 역순(-1)으로 출력된다














