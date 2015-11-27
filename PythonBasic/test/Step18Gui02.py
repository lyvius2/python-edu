'''
Created on 2015. 6. 20.

@author: 윤선
'''

# GUI 에 관련된 모듈 import 하기
import wx

# wx.Frame 클래스를 상속받은 커스텀 클래스를 정의하기

class MyFrame(wx.Frame):
    # parent => 부모 프레임, title => 프레임의 제목
    def __init__(self, parent, title):
        # 부모 생성자에 필요한 값 넘겨주기
        super(MyFrame, self).__init__(parent,\
            title=title, size=(300, 250))
        
        # 프레임에 TextCtrl 이라는 UI 추가하기
        self.txtA = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # 하단 상태바 보이게 하기
        self.CreateStatusBar()
        
        # 메뉴바 객체 생성
        menuBar = wx.MenuBar()
        # 메뉴 객체 생성
        mnuFile = wx.Menu()
        
        # 메뉴 아이템
        mnuNew = wx.MenuItem(mnuFile, wx.ID_NEW, "New", "새로운 문서")
        # 메뉴에 아이템 추가하기
        mnuFile.Append(mnuNew)
        # 메뉴에 아이템 추가하기2
        mnuFile.Append(wx.ID_OPEN, "Open", "Document Open")
        # 구분선
        mnuFile.AppendSeparator()
        # 메뉴에 아이템추가하기3
        mnuExit = mnuFile.Append(wx.ID_EXIT, "Exit", "종료합니다.")
        
        # 메뉴바에 메뉴 추가하기
        menuBar.Append(mnuFile, "File")
        # 메뉴바 장착
        self.SetMenuBar(menuBar)
        
        self.Center() # 화면 가운데에 띄우기
        self.Show() # 실제로 보이게 하기
        
        # 메뉴에 클릭 이벤트 처리
        self.Bind(wx.EVT_MENU, self.NewClicked, mnuNew)
        self.Bind(wx.EVT_MENU, self.ExitClicked, mnuExit)
        
    # New 를 클릭했을 때 실행할 메서드
    def NewClicked(self, event):
        print("New 를 클릭했네?")
        self.txtA.SetLabelText("새문서")
    
    # Exit 클릭했을 때 실행할 메서드
    def ExitClicked(self, event):
        self.Close(True)
        
app = wx.App()
# MyFrame 객체 생성
MyFrame(None, title="메뉴연습")
app.MainLoop()