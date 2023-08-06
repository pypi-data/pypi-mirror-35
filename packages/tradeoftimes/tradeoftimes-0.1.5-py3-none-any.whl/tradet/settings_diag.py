# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/ - hand modified to fit the application.
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SettingsDialog
###########################################################################

class SettingsDialog ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Trade of Times - Network Settings Page", pos = wx.DefaultPosition, size = wx.Size( 509,346 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.labelal = wx.StaticText( self, wx.ID_ANY, u"Network Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.labelal.Wrap( -1 )
        
        self.labelal.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        
        bSizer5.Add( self.labelal, 0, wx.ALL, 5 )
        
        fgSizer6 = wx.FlexGridSizer( 2, 3, 0, 0 )
        fgSizer6.AddGrowableCol( 1 )
        fgSizer6.SetFlexibleDirection( wx.HORIZONTAL )
        fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"External IP", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )
        
        fgSizer6.Add( self.m_staticText14, 0, wx.ALL, 5 )
        
        self.ext_ip = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer6.Add( self.ext_ip, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.externalIpHelpButton = wx.Button( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        fgSizer6.Add( self.externalIpHelpButton, 0, wx.ALL, 5 )
        
        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Peer Listen Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText15.Wrap( -1 )
        
        fgSizer6.Add( self.m_staticText15, 0, wx.ALL, 5 )
        
        self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer6.Add( self.m_textCtrl9, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.externalIpHelpButton1 = wx.Button( self, wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        fgSizer6.Add( self.externalIpHelpButton1, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( fgSizer6, 0, wx.EXPAND, 5 )
        
        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer17 = wx.BoxSizer( wx.VERTICAL )
        
        self.helplabel = wx.StaticText( self, wx.ID_ANY, u"Help Box", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.helplabel.Wrap( -1 )
        
        self.helplabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
        
        bSizer17.Add( self.helplabel, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.helpInfo = wx.StaticText( self, wx.ID_ANY, u"Click a \"?\" button to get helpful information on the field right next to it here.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.helpInfo.Wrap( -1 )
        
        self.helpInfo.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        bSizer17.Add( self.helpInfo, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer5.Add( bSizer17, 1, wx.EXPAND, 5 )
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.cancelButton, 0, wx.ALL, 5 )
        
        
        bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.applyButton = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.applyButton, 0, wx.ALL, 5 )
        
        self.okButton = wx.Button( self, wx.ID_ANY, u"Okay", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.okButton, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer6, 0, wx.BOTTOM|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer5 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.externalIpHelpButton.Bind( wx.EVT_BUTTON, self.external_ip_help )
        self.externalIpHelpButton1.Bind( wx.EVT_BUTTON, self.listen_port_help )
        self.cancelButton.Bind( wx.EVT_BUTTON, self.cancel )
        self.applyButton.Bind( wx.EVT_BUTTON, self.apply )
        self.okButton.Bind( wx.EVT_BUTTON, self.apply_quit )
    
    def __del__( self ):
        pass
    
    def external_ip_help( self, event ):
        self.helpInfo.SetLabel(
                'In the "External IP" field, you must insert the IP to which others can connect to send you\n'
                'events about their games. If not on NAT, just use your machine\'s Internet IP address.\n'
                'Otherwise, either port forward and use your NAT\'s external IP address, or use a tunnel\n'
                '(like ngrok) and insert your tunnel address (along with the port) here. '
        )
    
    def listen_port_help( self, event ):
        self.helpInfo.SetLabel(
                'In the "Listen Port" field, insert the port on which to listen to connections with other\n'
                'games. This is the port to which they will connect (along with the IP address through the\n1'
                'which your game peer is accessible). '
        )
    
    def cancel( self, event ):
        self.Close(True)
    
    def apply( self, event ):
        if not wx.App.Get().set_ext_addr(self.ext_ip.GetValue()):
            return
        
        wx.App.Get().set_listen_port(self.listen_port.GetValue())
        
        eaddr = self.ext_ip.GetValue()
        eport = eaddr.split(':')
        
        if len(eport) < 2:
            eport = None
            eaddr = eaddr[0]
            
        else:
            eport, eaddr = eaddr
            
            try:
                eport = int(eport)
                
            except ValueError:
                return
        
        wx.App.Get().write_config(eip=eaddr, listen_port=self.listen_port.GetValue(), ext_port=eport)
    
    def apply_quit( self, event ):
        self.apply(event)
        self.Close(True)
