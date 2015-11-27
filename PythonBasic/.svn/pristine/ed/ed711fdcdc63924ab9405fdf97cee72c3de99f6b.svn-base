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

import wx

class MemberFrame(wx.Frame):
    # 생성자
    def __init__(self, parent, title):
        super(MemberFrame, self).__init__(parent,\
                                          title=title, size=(600,500))
        self.InitUi()
        self.Center()
        self.Show()
        self.ShowMember() # 회원정보 출력하기
        
    # UI 초기화하는 메서드
    def InitUi(self):
        panel = wx.Panel(self)
        wx.StaticText(panel, label="이름", pos=(5, 5))        
        self.inputName = wx.TextCtrl(panel, pos=(55, 5))
        wx.StaticText(panel, label="주소", pos=(180, 5))
        self.inputAddr = wx.TextCtrl(panel, pos=(235, 5))
        saveBtn = wx.Button(panel, label="저장", pos=(350, 5))
        listBtn = wx.Button(panel, label="목록보기", pos=(450, 5)) 
        self.txtShow = wx.TextCtrl(panel, pos=(5, 50),\
        size=(550,150),style=wx.TE_MULTILINE|wx.TE_READONLY)
    
        # 버튼에 이벤트 등록하기
        saveBtn.Bind(wx.EVT_BUTTON, self.SaveBtnClicked)
        listBtn.Bind(wx.EVT_BUTTON, self.ListBtnClicked)
        
    # 저장버튼을 눌렀을 때 호출되는 메서드
    def SaveBtnClicked(self, event):
        # 입력한 이름과 주소를 읽어온다
        name = self.inputName.GetValue()
        addr = self.inputAddr.GetValue()
        print(name, addr)
        
        try:
            # connection 객체 얻어오기
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            sql = "INSERT INTO member (name, addr) VALUES (%s, %s)"
            sql_data = (name, addr)
            cursor.execute(sql, sql_data)
        except mysql.connector.Error as err :
            print("처리 오류:",err)
            conn.rollback()
        else:
            conn.commit()
            # 성공 메시지 띄우기
            dlg = wx.MessageDialog(self, "저장성공", "결과", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        finally:
            cursor.close()
            conn.close()
        self.ShowMember()
        
    # 목록보기 버튼을 눌렀을 때 호출되는 메서드
    def ListBtnClicked(self, event):
        self.ShowMember()
    
    # 회원목록을 출력하는 메서드
    def ShowMember(self):
        try:
            # connection 객체 얻어오기
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()
            sql = "SELECT num, name, addr FROM member ORDER BY num DESC"
            cursor.execute(sql)
            
            # 텍스트 필드에 출력된 내용 Clear
            self.txtShow.SetLabelText("")
            
            # 결과 셋 얻어오기
            resultSet = cursor.fetchall()
            for item in resultSet:
                str = "번호 : {} | 이름 : {} | 주소 : {}\n".format(*item)
                # UI에 append 하기
                self.txtShow.AppendText(str)
                
        except mysql.connector.Error as err :
            print("처리 오류:",err)
        else:
            pass
        finally:
            cursor.close()
            conn.close()
            
app = wx.App()
MemberFrame(None, title="회원정보")
app.MainLoop()