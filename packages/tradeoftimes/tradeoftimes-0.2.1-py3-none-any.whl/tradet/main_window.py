# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/ - hand modified to fit the application.
###########################################################################

import wx
import wx.xrc

from tradet.settings_diag import SettingsDialog
from tradet.game_diag import GameDialog
from tradet.nick_diag import NickDialog

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Trade of Times", pos = wx.DefaultPosition, size = wx.Size( 1078,593 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        self.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
        self.SetBackgroundColour( wx.Colour( 219, 219, 219 ) )
        
        self.status_bar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.ulabel = wx.StaticText( self, wx.ID_ANY, u"Users", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.ulabel.Wrap( -1 )
        
        self.ulabel.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        
        bSizer2.Add( self.ulabel, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.userList = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer2.Add( self.userList, 1, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.gameCanvas = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.gameCanvas.SetBackgroundColour( wx.Colour( 46, 46, 46 ) )
        
        bSizer3.Add( self.gameCanvas, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer3, 7, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.clabel = wx.StaticText( self, wx.ID_ANY, u"Chat", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.clabel.Wrap( -1 )
        
        self.clabel.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        
        bSizer4.Add( self.clabel, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.chatWindow = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        self.chatWindow.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        bSizer4.Add( self.chatWindow, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.chatField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.chatField, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer4, 3, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Connect to...", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem1 )
        
        self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit Network", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem4 )
        
        self.m_menu1.AppendSeparator()
        
        self.m_menuItem5 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Set Name...", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem5 )
        
        self.m_menuItem6 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Network Settings...", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.m_menuItem6 )
        
        self.m_menubar1.Append( self.m_menu1, u"Multiplayer" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.deinit )
        self.chatField.Bind( wx.EVT_TEXT_ENTER, self.send_chat )
        self.Bind( wx.EVT_MENU, self.connection_dialog, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.connection_dialog, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.quit_network, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.set_nick_dialog, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_MENU, self.settings_dialog, id = self.m_menuItem6.GetId() )
    
    def __del__( self ):
        pass
    
    def deinit(self, event):
        wx.App.Get().server.disconnect()
        wx.App.Get().server.stop_loop()
        event.Skip()
    
    # Virtual event handlers, overide them in your derived class
    def send_chat( self, event ):
        wx.App.Get().send_chat(self.chatField.GetValue())
        self.chatField.SetValue('')
    
    def connection_dialog( self, event ):       
        GameDialog(None).ShowModal()
    
    def quit_network( self, event ):
        wx.App.Get().quit()
        self.Close(True)
    
    def set_nick_dialog( self, event ):
        NickDialog(None).ShowModal()
    
    def settings_dialog( self, event ):
        SettingsDialog(None).ShowModal()
