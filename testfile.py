import threading
import time
import wx


def run(n):
    print("task", n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)


# if __name__ == '__main__':
#     t1 = threading.Thread(target=run, args=("t1",))
#     t2 = threading.Thread(target=run, args=("t2",))
#     t1.start()
#     t2.start()
# -*- coding:utf-8 -*-


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='', size=(400, 300), name='frame', style=541072960)
        self.启动窗口 = wx.Panel(self)
        self.Centre()
        self.按钮1 = wx.Button(self.启动窗口, size=(80, 32), pos=(269, 40), label='按钮', name='button')
        self.按钮1.Bind(wx.EVT_BUTTON, self.按钮1_按钮被单击)

    def 按钮1_按钮被单击(self, event):
        from main import  camera
        camera()


class myApp(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True


if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
