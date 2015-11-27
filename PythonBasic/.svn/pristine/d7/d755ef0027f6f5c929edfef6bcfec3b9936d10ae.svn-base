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
    
    # 3번 회원의 정보를 얻어오려면
    sql = "SELECT num, name, addr FROM member WHERE num = %s"
    sql_data = (2,)
    cursor.execute(sql, sql_data)
    # resultSet = cursor.fetchall()
    # select 된 row가 1개인 경우 'fetchone'
    result = cursor.fetchone()
    # 회원 한명의 정보가 tuple type으로 바로 얻어내진다
    print(result)
    num = result[0]
    name = result[1]
    addr = result[2]
    # str = "번호:{}, 이름:{}, 주소:{}".format(num,name,addr)
    # *result tuple type 매칭
    str = "번호:{}, 이름:{}, 주소:{}".format(*result)
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
    