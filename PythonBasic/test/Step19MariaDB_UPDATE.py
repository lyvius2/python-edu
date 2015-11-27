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
    sql = "UPDATE member SET name = %s, addr = %s WHERE num = %s"
    # %s에 바인딩할 내용을 순서대로 tuple type data로 준비
    sql_data = ('원숭이','동물원',2)
    # cursor 객체를 이용해서 sql문 수행하기
    cursor.execute(sql, sql_data)
    print("2번 회원의 정보를 수정하였습니다.")

    
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
    