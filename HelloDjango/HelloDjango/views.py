'''
Created on 2015. 6. 27.

@author: 윤선
'''
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from _datetime import datetime

# plain text return
def hello(request):
    res = HttpResponse("Hello, World!")
    return res

def merong(request):
    res = HttpResponse("Oh, no!")
    return res
'''
def sample(request):
    html = "<!doctype html>\n"+\
    "<html>\n"+\
    "<head>\n"+\
    "<meta charset='utf-8'>\n"+\
    "</head>\n"+\
    "<body>\n"+\
    "<h1>김구라</h1>\n"+\
    "</body>\n"+\
    "</html>"
    
    return HttpResponse(html)
'''

def sample(request):
    # template 디렉터리 안에 있는 sample.html을 읽어들여서
    # 해석된 결과를 출력한다.
    return render_to_response("sample.html")

def sample2(request):
    return render_to_response("sample2.html", {"name":"원숭이"})

def currentTime(request):
    # 현재 시간 얻어오기
    d = datetime.now()
    return render_to_response("currentTime.html", {"time":d})
    
def friendList(request):
    # DB에서 읽어온 친구 목록이라고 가정하고
    friends = ("김구라", "해골", "원숭이", "주뎅이", "덩어리")
    return render_to_response("friendList.html", {"friends":friends})

# 필요한 모듈 import
import mysql.connector
from mysql.connector import errorcode

# DB 접속 정보를 dict type으로 준비한다.
config={"user":"root",
        "password":"maria",
        "host":"127.0.0.1",
        "database":"guro",
        "port":"3306"}

# Maria DB에 있는 내용을 읽어와서 HTML 형식으로 렌더링해주는 함수
def memberList(request):
    members = None
    try:
        # maria db connection 객체 얻어오기
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        # 모든 회원의 정보를 num에 대해서 내림 차순을 적용해서 출력
        sql = "SELECT num, name, addr FROM member ORDER BY num DESC"
        cursor.execute(sql)
        # cursor에 있는 SELECT 된 내용 얻어오기
        members = cursor.fetchall()
    except mysql.connector.Error as err:
        print("처리 오류:"+err)
    finally:
        # 사용한 객체 닫아주기
        cursor.close()
        conn.close()
    print(members)
    return render_to_response("memberList.html",{"members":members})