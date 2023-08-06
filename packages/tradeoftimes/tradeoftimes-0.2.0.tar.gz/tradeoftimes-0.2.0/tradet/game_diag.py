# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/ - edited by hand to fit application.
###########################################################################

import traceback
import warnings
import wx
import wx.xrc

###########################################################################
## Class GameDialog
###########################################################################

class GameDialog ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Trade of Times - Connect to Another Game", pos = wx.DefaultPosition, size = wx.Size( 463,129 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Insert the network game to connect to.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_ELLIPSIZE_END )
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
        
        self.addrField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        fgSizer1.Add( self.addrField, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer5.Add( fgSizer1, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.cancelButton, 0, wx.ALL, 5 )
        
        
        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.gameButton = wx.Button( self, wx.ID_ANY, u"Change", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.gameButton, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.addrField.Bind( wx.EVT_TEXT_ENTER, self.connect )
        self.cancelButton.Bind( wx.EVT_BUTTON, self.cancel )
        self.gameButton.Bind( wx.EVT_BUTTON, self.connect )
    
    def __del__( self ):
        pass
    
    def cancel( self, event ):
        self.Close(True)
    
    def connect( self, event ):        
        addr = self.addrField.GetValue().split(':')
        
        if len(addr) == 1:
            addr.append(2913)
            
        elif len(addr) == 2:
            try:
                addr[1] = int(addr[1])
                
            except BaseException as err:
                traceback.print_exc()
                self.Close(True)
                return
                
        else:
            warnings.warn("Bad address: '{}'!".format(addr))
            self.Close(True)
            return
    
        wx.App.Get().connect(addr)
        self.Close(True)
        