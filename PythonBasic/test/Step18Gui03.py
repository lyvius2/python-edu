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
        
        # btn1에 이벤트 등록하기
        btn1.Bind(wx.EVT_BUTTON, self.OnClicked1)
        # btn2에 이벤트 등록하기
        btn2.Bind(wx.EVT_TOGGLEBUTTON, self.OnClicked2)
        btn3.Bind(wx.EVT_BUTTON, self.OnClicked3)
        
    def OnClicked1(self, event):
        # print("버튼을 눌렀네?")
        dlg = wx.MessageDialog(self, "일반 버튼 처리", "처리", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnClicked2(self, event):
        # 토글 버튼의 상태를 bool type으로 얻어올 수 있다.
        isActive = event.GetEventObject().GetValue()
        print("isActive : ", isActive)
        
    def OnClicked3(self, event):
        self.Close(True)
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title="버튼")
    app.MainLoop()