# -*- coding: utf-8 -*-
__author__ = 'Evenvi'
import wx
import lang

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self,None, -1, lang.windowName,size=(300,300))
        panel = wx.Panel(self,-1)
        panel.Bind(wx.EVT_MOTION, self.onMove)
        wx.StaticText(panel, -1, lang.mousePos, pos =(10,12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(100, 10))

    def onMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))