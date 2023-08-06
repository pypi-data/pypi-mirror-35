# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class NickDialog
###########################################################################

class NickDialog ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Trade of Times - Pick a New Nickname", pos = wx.DefaultPosition, size = wx.Size( 463,129 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Pick a new nickname.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText2.Wrap( -1 )
        
        self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        
        bSizer5.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
        
        fgSizer1 = wx.FlexGridSizer( 1, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 1 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Nickname:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        
        fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.nickField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        fgSizer1.Add( self.nickField, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer5.Add( fgSizer1, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.cancelButton, 0, wx.ALL, 5 )
        
        
        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.nickButton = wx.Button( self, wx.ID_ANY, u"Change", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.nickButton, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.nickField.Bind( wx.EVT_TEXT_ENTER, self.setnick )
        self.cancelButton.Bind( wx.EVT_BUTTON, self.cancel )
        self.nickButton.Bind( wx.EVT_BUTTON, self.setnick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def setnick( self, event ):
        wx.App.Get().set_nick(self.nickField.GetValue())
        self.Close(True)
    
    def cancel( self, event ):
        self.Close(True)
