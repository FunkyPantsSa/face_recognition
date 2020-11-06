import wx
import os
from importlib import reload
import webbrowser
import face_img_register
import face_recognize_punchcard
import sys

main = "icon/main.png"
file_path = os.getcwd() + r'\data\logcat.csv'


class Mainui (wx.Frame):
    def __init__(self, superion ):
        wx.Frame.__init__(self, parent=superion, title="考勤系统", size=(800, 590))
        self.SetBackgroundColour('white')
        self.Center()

        self.frame = ''
        self.RegisterButton = wx.Button(parent=self, pos=(50, 120), size=(80, 50), label='人脸录入')

        self.PunchcardButton = wx.Button(parent=self, pos=(50, 220), size=(80, 50), label='刷脸签到')

        self.LogcatButton = wx.Button(parent=self, pos=(50, 320), size=(80, 50), label='日志查看')

        self.InstructButton = wx.Button(parent=self, pos=(210, 460), size=(80, 50), label='操作说明')





        self.Bind(wx.EVT_BUTTON, self.OnRegisterButtonClicked, self.RegisterButton)
        self.Bind(wx.EVT_BUTTON, self.OnPunchCardButtonClicked, self.PunchcardButton)
        self.Bind(wx.EVT_BUTTON, self.OnLogcatButtonClicked, self.LogcatButton)
        self.Bind(wx.EVT_BUTTON, self.OnInstructButtonClicked, self.InstructButton)


        # 封面图片
        self.image_cover = wx.Image(main, wx.BITMAP_TYPE_ANY).Scale(520, 360)
        # 显示图片
        self.bmp = wx.StaticBitmap(parent=self, pos=(180, 80), bitmap=wx.Bitmap(self.image_cover))