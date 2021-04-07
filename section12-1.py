# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

# 명령 프롬프트(CMD) : 실행 시 관리자 권한으로 실행(에러 방지)
import sqlite3
import datetime

# 삽입 날짜 생성
print('<현재 시간 날짜 확인>')
now = datetime.datetime.now()
print('now : ', now)
print('<현재 시간 설정 : strftime() >')
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S') # 현재 시간 설정
print('nowDatetime : ', nowDatetime)
print()
print('----------------------------------------------------')

# sqlite3
print('<SQLite 버전 확인>')
print('sqlite3.version :', sqlite3.version)
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version)
print()
print('----------------------------------------------------')

# DB 생성 & Auto Commit(RollBack(이전으로 돌아가기))
print('<DB 경로 설정 : connect("경로") >')
conn = sqlite3.connect('C:\work/python_basic/.vscode/resource/database.db', isolation_level=None) # DB생성
conn.commit()

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))
print()
print('----------------------------------------------------')

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
# print('<테이블 생성>')
# CREATE TABLE IF NOT EXISTS : 테이블이 없을 경우 테이블을 만들겠다는 의미
# c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, usename text, email text,\
#                       phone text, website text, regdate text)")

# # ? : ?자리에 있는 date를 ()괄호안에 있는 nowDatetime랑 매치
print('<데이터 삽입>')
c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '010-0000-0000', 'kim.com', ?)", (nowDatetime,))
c.execute("INSERT INTO users(id, usename, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", (2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDatetime))

# # Many 삽입(튜플, 리스트)
print('<데이터 대량 삽입 : tuple, List 형식으로 가능>')
userList = (
       (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
       (4, 'Yoon', 'Yoon@naver.com', '010-3333-3333', 'Yoon.com', nowDatetime),
       (5, 'cho', 'cho@naver.com', '010-4444-4444', 'cho.com', nowDatetime)
   )

# c.executemany : executemany("쿼리문, seq_of_parameters")
print("<데이터 대량 삽입 : executemany("'쿼리문'", 객체'>")
c.executemany("INSERT INTO users(id, usename, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
# conn.execute('DELETE FROM users')

# 데이터를 몇개 지웠는지 확인 : rowcount()
# print('users db deleted : ', conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_lever = None 일 경우 자동 반영(자동 저장)
# conn.commit()   : 수동으로 실행
# conn.rollback() : 저장 전으로 실행

# 접속 해제
conn.close()

data = input() # 문자열로 받는다
count0 = 0
count1 = 0

for i in data:
    if int(i) == 1:
        count0 += 1
    else:
        count1 += 1

