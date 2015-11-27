'''
Created on 2015. 6. 27.

@author: 윤선
'''

# 연결객체 확인하기
import mysql.connector

# Maria DB 연결해서 연결 객체 얻어오기
conn = mysql.connector.Connect(user='root',password='maria',\
                               host='127.0.0.1', database='guro', port=3306)
# 정상적으로 얻어와 지는지 정보 출력하기
print(conn)
conn.close()