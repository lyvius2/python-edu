'''
Created on 2015. 6. 27.

@author: 윤선
'''
# 필요한 모듈 import
import mysql.connector
from mysql.connector import errorcode

# DB 접속 정보를 dict type으로 준비한다.
config={"user":"root",
        "password":"maria",
        "host":"127.0.0.1",
        "database":"guro",
        "port":"3306"}

try:
    # maria db connection 객체 얻어오기
    conn = mysql.connector.connect(**config)    # **는 dict 자료 매칭
    # db에 select, insert, update, delete 작업을 수행할 cursor 객체
    cursor = conn.cursor()
    
    # 모든 회원의 정보를 num에 대해서 내림 차순을 적용해서 출력
    sql = "SELECT num, name, addr FROM member ORDER BY num DESC"
    cursor.execute(sql)
    # cursor에 있는 SELECT 된 내용 얻어오기
    resultSet = cursor.fetchall()
    # 구조 출력해오기
    print(resultSet) # list type 에 회원정보가 순서대로 tuple type으로 들어있다.
    
    # 반복문 돌면서 회원정보를 원하는 포맷으로 출력해보기
    print("---member 테이블에 저장된 내용---")
    for item in resultSet:
        # tuple type 데이터에 각각의 방에 저장된 회원정보를 얻어온다.
        num = item[0]
        name = item[1]
        addr = item[2]
        str = "번호:{}, 이름:{}, 주소:{}".format(num, name, addr)
        print(str)
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("id 혹은 비밀번호 오류")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("DB 오류")
    else:
        print("기타 오류:"+err)
    # 예외가 발생하면 DB 반영을 취소한다.
    conn.rollback()
else:
    # 예외가 발생하지 않으면 DB 에 반영한다.
    conn.commit()
finally:
    # 사용한 객체 닫아주기
    cursor.close()
    conn.close()
    