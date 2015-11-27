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
    
    '''
    # 회원정보를 member table에 저장하기
    sql1 = "INSERT INTO member (name, addr) VALUES ('김구라','노량진')"
    # cursor 객체를 이용해서 sql 문 수행하기
    cursor.execute(sql1)
    # db에 실제 반영하기
    conn.commit()
    '''
    
    # 테이블에 저장할 정보가 변수 안에 들어있는 경우
    name1 = "해골"
    name2 = "행신동"
    
    sql2 = "INSERT INTO member (name, addr) VALUES (%s, %s)"
    # %s에 바인딩 할 내용을 tupㅣe type으로 준비한다.
    sql_data=(name1, name2)
    # cursor 객체의 execute() 메서드를 호출하면서 필요한 값 전달하기
    cursor.execute(sql2, sql_data)
    print("회원 한명의 정보를 저장하였습니다.")
    
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
    