'''
Created on 2015. 6. 20.

@author: 윤선
'''
import wx

class MyFrame(wx.Frame):
    
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent,\
            title=title, size=(700,500))
        # UI 초기화하는 메서드 호출
        self.InitUi()
        self.Center()
        self.Show()
        
    # UI 초기화 하는 메서드 정의
    def InitUi(self):
        # Panel 객체
        panel = wx.Panel(self)
        
        # 일반 버튼
        btn1 = wx.Button(panel, label="눌러보셈", pos=(5,5))
        # 토글 버튼
        btn2 = wx.ToggleButton(panel, label="토글버튼", pos=(120, 5))
        btn3 = wx.Button(panel, label="종료", pos=(235, 5))
        
        # 각각의 버튼 객체에 id를 임의로 부여한다.
        btn1.id = 1
        btn2.id = 2
        btn3.id = 3
        
        # btn1에 이벤트 등록하기
        btn1.Bind(wx.EVT_BUTTON, self.OnClicked)
        # btn2에 이벤트 등록하기
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClicked)
        btn3.Bind(wx.EVT_BUTTON, self.OnClicked)
        
        # 정적인 텍스트 출력
        wx.StaticText(panel, label="아이디", pos=(5, 40))
        wx.StaticText(panel, label="비밀번호", pos=(5, 70))
        
        # 텍스트 컨트롤
        self.inputId = wx.TextCtrl(panel, pos=(100, 40))
        self.inputPwd = wx.TextCtrl(panel, pos=(100, 70))
        
        # 로그인 버튼
        loginBtn = wx.Button(panel, label="로그인", pos=(100, 100))
        # 버튼에 이벤트 등록
        loginBtn.Bind(wx.EVT_BUTTON, self.LoginBtnClicked)
    
    # 로그인 버튼을 눌렀을 때 실행할 메서드 정의
    def LoginBtnClicked(self, event):
        # 1. 입력한 id와 비밀번호를 읽어온다.
        id = self.inputId.GetValue()
        pwd = self.inputPwd.GetValue()
        msg = None
        # 2. DB에 있는 내용과 일치하는지 확인한다.
        if id == "gura" and pwd == "1234":
            msg = "gura 회원님 반갑습니다."
        else:
            msg = "id 혹은 비밀번호가 틀려요!"
        # 3. 사용자에게 알리기
        dlg = wx.MessageDialog(self, msg, "알림", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def OnClicked(self, event):
        # 이벤트가 일어난 버튼의 참조값을 얻어온다.
        btn = event.GetEventObject()
        # 눌러진 버튼에 부여된 id를 읽어와서 선택적인 작업을 한다.
        if btn.id == 1:
            dlg = wx.MessageDialog(self, "일반 버튼 처리", "처리", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        elif btn.id == 2:
            isActive = event.GetEventObject().GetValue()
            print("isActive : ", isActive)
        elif btn.id == 3:
            self.Close(True)
            
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title="버튼")
    app.MainLoop()