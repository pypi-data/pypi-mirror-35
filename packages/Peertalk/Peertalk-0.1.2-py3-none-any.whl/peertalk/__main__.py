import numpy as np
import threading
import os
import json
import random
import string
import wx
import peertalk as pt
import peertable as pb


class InitDialog(wx.Dialog):
    def __init__(self, parent, container, app):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"First-Time Setup", pos = wx.DefaultPosition, size = wx.Size( 559,217 ), style = wx.DEFAULT_DIALOG_STYLE )
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Please fill in the fields below so you can receive data, have an online pseudonym, et cetera.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nickname:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        self.startnick = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.startnick, 1, wx.ALL, 5 )
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"External address (to receive data):", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
        self.remoteaddr = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.remoteaddr, 1, wx.ALL, 5 )
        bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Peer listen port:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer31.Add( self.m_staticText31, 0, wx.ALL, 5 )
        self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 2800, 2999, 2912 )
        bSizer31.Add( self.m_spinCtrl1, 1, wx.ALL, 5 )
        bSizer1.Add( bSizer31, 0, wx.EXPAND, 5 )
        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Begin", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button1, 1, wx.ALL, 5 )
        bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )
        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        self.m_button1.Bind( wx.EVT_BUTTON, self.submit )
        
        self.app = app
        self.container = container
    
    def submit(self, event):
        nick, addr, port = [p.GetValue() for p in (self.startnick, self.remoteaddr, self.m_spinCtrl1)]
        
        while len(self.container) > 0:
            self.container.pop()
            
        for _ in range(3):
            self.container.append(0)
            
        self.container[0] = nick
        self.container[1] = addr
        self.container[2] = port
        
        self.app.post_dialog()
        self.Close(True)

class MainWindow(wx.Frame):
    def __init__(self, parent, app):
        # massive blob of layout code >_>
        # DO NOT TOUCH! 
        self.app = app
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1007,568 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        self.ipalabel = wx.StaticText( self, wx.ID_ANY, "IP Address", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ipalabel.Wrap( -1 )
        bSizer4.Add( self.ipalabel, 0, wx.ALL, 5 )
        self.ipCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.ipCtrl, 0, wx.ALL, 5 )
        bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_button1 = wx.Button( self, wx.ID_ANY, "Connect!", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_button1, 10, wx.ALL, 5 )
        bSizer2.Add( bSizer5, 0, wx.EXPAND, 5 )
        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer2.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, "Nickname", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )
        self.nickCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.nickCtrl, 0, wx.ALL, 5 )
        bSizer2.Add( bSizer6, 0, wx.EXPAND, 5 )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_button2 = wx.Button( self, wx.ID_ANY, "Set Nickname", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button2, 1, wx.ALL, 5 )
        bSizer2.Add( bSizer8, 0, wx.EXPAND, 5 )
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, "Users", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer10.Add( self.m_staticText3, 0, wx.ALL, 5 )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        self.userList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer11.Add( self.userList, 1, wx.ALL|wx.EXPAND, 5 )
        bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )
        bSizer2.Add( bSizer10, 1, wx.EXPAND, 5 )
        self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer2.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        self.m_button3 = wx.Button( self, wx.ID_ANY, "Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button3, 1, wx.ALL, 5 )
        bSizer2.Add( bSizer9, 0, wx.EXPAND, 5 )
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        self.buffer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer3.Add( self.buffer, 1, wx.ALL|wx.EXPAND, 5 )
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        self.mynick = wx.StaticText( self, wx.ID_ANY, app.nickname, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.mynick.Wrap( -1 )
        bSizer12.Add( self.mynick, 0, wx.ALL, 5 )
        self.mymsg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer12.Add( self.mymsg, 1, wx.ALL, 5 )
        bSizer3.Add( bSizer12, 0, wx.EXPAND, 5 )
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
        
        # Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.connect )
        self.m_button2.Bind( wx.EVT_BUTTON, self.set_nick )
        self.m_button3.Bind( wx.EVT_BUTTON, self.quit )
        self.mymsg.Bind( wx.EVT_TEXT_ENTER, self.send_message )
        
        self.Show(True)
    
    def set_nick(self, event):
        nick = self.nickCtrl.GetValue()
        
        if nick == '':
            return
            
        self.mynick.SetLabel(nick)
        self.app.set_nick(nick)
        
        event.Skip()
    
    def connect(self, event):
        if self.app.server is None:
            event.Skip()
            return
    
        addr = self.ipCtrl.GetValue().split(':')
        print("Connecting to: {}".format(addr))
        
        try:
            addr[1] = int(addr[1])
            
        except BaseException as err:
            event.Skip()
            return
            
        self.app.server.connect(tuple(addr))
        
        event.Skip()
    
    def quit(self, event):
        self.app.quit()
        self.Close(True)
        
        event.Skip()
        
    def send_message(self, event):
        msg = self.mymsg.GetValue()
        self.mymsg.SetValue("")
        
        self.app.send_message(msg)
        
        event.Skip()

class WxChatApp(pt.ChatApp):
    def __init__(self):
        super().__init__("")
        print("Starting session.")
        
        self.app = wx.App(False)
        self.frame = MainWindow(None, self)
        self.pos = 0
        
    def start(self):
        print("Initialization dialog:")
        self.initial = []
        dialog = InitDialog(None, self.initial, self)
        dialog.ShowModal()
        self.app.MainLoop()
        
    def post_dialog(self):
        nick, addr, port = self.initial
        eport = None
        
        if ":" in addr:
            addr = addr.split(':')
            eport = int(addr[1])
            addr = addr[0]
        
        print("Starting peer...")
        server = pb.PeerServer(addr, port=port)
        server.register_app(self)
        server.start_loop()
        self.frame.mynick.SetLabel(nick)
        self.set_nick(nick)
        
    def on_app_message(self):
        while self.pos < len(self.messages) - 1:
            self.pos += 1
            
            m = self.messages[self.pos]
            mtype = m[0]
            
            if mtype == "MESSAGE":
                self.frame.buffer.SetValue(self.frame.buffer.GetValue() + "\n<{}> {}".format(self.nicknames[m[2]], m[4]))
                
            elif mtype == "QUIT":
                self.frame.buffer.SetValue(self.frame.buffer.GetValue() + "\n--- {} has quit".format(self.nicknames[m[3]]))
                
            elif mtype == "JOIN":
                self.frame.buffer.SetValue(self.frame.buffer.GetValue() + "\n+++ {} has joined".format(self.nicknames[m[3]]))
        
def main():
    app = WxChatApp()
    app.start()
    
if __name__ == "__main__":
    main()