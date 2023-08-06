import wx
import string
import random
import json
import time
import peertable
import os
import traceback
import ipgetter

from tradet.main_window import MainWindow


class TradeGamePeer(peertable.PeerApplication):
    def __init__(self):
        self.messages = []
        self.glues = []
        self.app = wx.App.Get()

    def timeout_messages(self):
        mm = []
    
        for m in self.messages:
            if time.time() - m[1] < 90:
                mm.append(m)
                
        self.messages = mm
        
    def game_turn(self, server, client, data, message):
        pass # no game yet...
        
    def receive_data(self, server, client, id, mtype, data, message):
        if mtype == "CHAT":
            server.broadcast(message)
            c_id = data.decode('utf-8').split(':')[0]
            content = ':'.join(data.split(':')[1:])
            self.app.frame.chatWindow.SetValue(self.app.frame.chatWindow.GetValue()\
                + "    <{}> {}\n".format(self.app.nicks.get(c_id, c_id), content)
            )
            
        elif mtype == "QUIT":
            self.app.nicks.pop(data.decode('utf-8'))
            self.app.nick_update()
            self.app.remove_user(data.decode('utf-8'))
            
        elif mtype == "HOSTDEAD":
            self.app.elected = False
            server.broadcast(message)
            server.broadcast(peertable.Message(True, "WHOSHOST", server.id))
            
        elif mtype == "SETNAME":
            id, nick = data.decode('utf-8').split(':')
            n = self.app.nicks.get(id)
            self.app.nicks[id] = nick
            self.app.nick_update()
            
            if n is not None:
                self.app.frame.chatWindow.SetValue(self.app.frame.chatWindow.GetValue()\
                    + "*** {} is now known as {}\n".format(n, self.app.nicks.get(client.id, client.id))
                )
                
            else:
                self.app.frame.chatWindow.SetValue(self.app.frame.chatWindow.GetValue()\
                    + "+++ {} has joined\n".format(n, self.app.nicks.get(client.id, client.id))
                )
            
            server.broadcast(message)
            
        elif mtype == "GAMETURN" and client.id == self.app.host:
            self.game_turn(server, client, data, message)
        
    def add_message(self, msg):
        self.app.frame.chatWindow.SetValue(self.app.frame.chatWindow.GetValue()\
            + msg + "\n"
        )
        
    def broadcast_name(self, server):
        server.broadcast(peertable.Message(True, 'SETNAME', ''.join([random.choice(string.digits + string.ascii_letters) for _ in range(50)]) + ":".join([server.id, self.app.nick])))
        
    def check_message(self, server, client, message):
        self.timeout_messages()
        id = message.payload[:50].decode('utf-8')
        
        if id in [x[0] for x in self.messages]:
            return
            
        self.receive_data(server, client, message.payload[:50].decode('utf-8'), message.message_type.rstrip(' '), message.payload[50:], message)
        
    def receive(self, server, client, message):
        if message.message_type == "NETWGLUE":
            glue = message.payload.decode('utf-8')
            self.app.last_host_req = time.time()
            server.broadcast(peertable.Message(True, 'WHOSHOST', server.id))
        
            if glue in self.glues:
                return
        
            self.broadcast_name(server)
            server.broadcast(message)
            
        elif message.message_type == 'WHOSHOST':
            if self.app.elected and self.app.host == server.id:
                server.send_id(message.payload.decode('utf-8'), peertable.Message(True, "IAMHOST"))
                
            elif not self.app.elected:
                server.broadcast(peertable.Message(True, "MKMEHOST", server.id))
        
        elif message.message_type == "IAMHOST" and time.time() - self.app.last_host_req < 30 and not self.app.elected:
            self.app.host = client.id
            self.app.elected = True
           
        elif message.message_type == "MKMEHOST" and not self.app.elected:
            id = message.payload.decode('utf-8')
            
            if self.app.host != id:
                self.app.host = id
                self.app.elected = True
                server.broadcast(message)
        
        elif message.message_type == "MYNAMEIS":
            self.app.nicks[client.id] = message.payload.decode('utf-8')
            self.app.nick_update()
    
        elif message.message_type == "USERDEAD":
            self.app.nicks.pop(message.payload.decode('utf-8'))
            self.app.nick_update()
    
        else:
            self.check_message(server, client, message)
            
    def disconnected(self, server, client):
        server.broadcast(peertable.Message(True, 'USERDEAD', client.id))
        
        if self.app.elected and self.app.host == client.id:
            server.broadcast(peertable.Message(True, 'HOSTDEAD'))
            self.app.elected = False

class TradeGameApp(wx.App):
    def OnInit(self, config_file=None):
        self.nicks = {}
    
        self.config_file = config_file or 'settings.json'
    
        if os.path.isfile(self.config_file):
            config = json.load(open(self.config_file))
            self.server = peertable.PeerServer(config['External IP'], port=config['Listen Port'], remote_port=config['External Port'])
            nick = config['Nickname']
        
        else:
            eip = ipgetter.myip()
            nick = random.choice(("_Guest", "_Newbie", "_Invitee", "_Rookie")) + '_' + ''.join([random.choice(string.digits) for _ in range(7)])
            
            self.server = peertable.PeerServer(eip, port=2913)
            # set defaults
            open(self.config_file, 'w').write(json.dumps({
                "External IP": eip,
                "Listen Port": 2913,
                "External Port": 2913,
                "Nickname": nick,
            }))
            
        self.nick = nick
        self.host = self.server.id # Corrected Once Connected
        self.elected = False
            
        self.init_frame()
        self.update_bar()
        self.peer_app = TradeGamePeer()
        self.nick_update()
        self.server.register_app(self.peer_app)
        self.server.start_loop()
        
        return True
        
    def update_bar(self):
        self.frame.status_bar.SetStatusText("Nickname: {} | Listen Port: {} | Public Address: {}".format(self.nick, self.server.port, self.server.address + ":" + str(self.server.remote_port)))
        
    def write_config(self, eip=None, listen_port=None, ext_port=None):
        open(self.config_file, 'w').write(json.dumps({
            "External IP": eip or self.server.address,
            "Listen Port": listen_port or self.server.port,
            "External Port": ext_port or self.server.remote_port,
            "Nickname": self.nick
        }))
        
        # print("Updated settings.json file.")
        
    def nick_update(self):
        res = self.nick + "\n"
        
        for n in self.nicks.values():
            res += n + "\n"
            
        self.frame.userList.SetValue(res)
        
    def set_ext_addr(self, extip):
        try:
            if ':' in extip:
                addr = extip.split(':')
                port = int(addr[1])
                addr = addr[0]
        
            else:
                addr = extip
                port = self.server.remote_port
            
        except BaseException as err:
            traceback.print_exc()
            return False
    
        self.server.address = addr
        self.server.remote_port = port
        
        return True
        
    def init_frame(self):
        self.frame = MainWindow(None)
        self.frame.Show()
        
    def send_chat(self, message):
        self.peer_app.add_message("    <{}> {}".format(self.nick, message))
        self.server.broadcast(peertable.Message(True, 'CHAT', ''.join([random.choice(string.digits + string.ascii_letters) for _ in range(50)]) + ':'.join([self.server.id, message])))
    
    def quit(self):
        self.frame.Close(True)
        
    def connect(self, addr):
        self.server.connect(addr)
        self.server.broadcast(peertable.Message(True, 'NETWGLUE', self.server.id))
        self.last_host_req = time.time()
        self.server.broadcast(peertable.Message(True, 'WHOSHOST', self.server.id))
        
    def set_nick(self, n):
        self.nick_update()
        self.peer_app.add_message("*** You, previously {}, are now known as {}".format(self.nick, n))
        self.nick = n
        self.peer_app.broadcast_name(self.server)
        self.write_config()
        self.update_bar()
        
    def set_listen_port(self, port):
        pass