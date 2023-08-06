import peertable as peer
import json
import random
import string
import wx
import time


class ChatApp(peer.PeerApplication):
    def __init__(self, nickname):
        self.nickname = nickname
        self.messages = []
        self.nicknames = {}
        self.users = []
        self.server = None

    def on_app_message(self):
        pass
        
    def send_message(self, msg):
        if self.server is None:
            return
    
        mid = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)])
        
        self.server.broadcast(peer.Message(True, "MESSAGE", json.dumps({
            'sender_id': self.server.id,
            'message_id': mid,
            'content': msg,
            'closed': [self.server.id]
        })))
        
    def quit(self):
        if self.server is None:
            return
            
        self.server.broadcast(peer.Message(True, "QUIT", "{}:{}:{}".format(self.server.id, ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)]), self.server.id)))
        
    def set_nick(self, nick):
        self.nickname = nick
        self.server.broadcast(peer.Message(True, "MYNAMEIS", "{}:{}:{}".format(self.server.id, ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)]), self.server.id)))
        
    def receive(self, server, client, message):
        if message.message_type == "GETNICK ":
            server.send_id(client.id, peer.Message(True, "MYNAMEIS", self.nickname))
            client.disconnect() # here to prevent that too many clients populate our lists
            
        elif message.message_type == "MYNAMEIS":
            self.nicknames[client.id] = message.payload.encode('utf-8')
            
            if client.id not in self.users:
                self.users.append(client.id)
                
        elif message.message_type == "QUIT    ":
            quitter, quit_id, closed = message.payload.decode('utf-8')
            closed = closed.split('#')
            
            if quit_id in [x[2] for x in self.messages]:
                return
            
            self.messages.append(("QUIT", time.time(), quit_id, quitter))
            
            for c in server.clients:
                if c.id == quitter:
                    c.disconnect()
            
                elif c.id not in closed:
                    closed.append(c.id)
                    
            server.broadcast(peer.Message(True, "QUIT", "{}:{}:{}".format(quitter, quit_id, '#'.join(closed))))
    
        elif message.message_type == "__QUERYR":
            cid = message.payload.decode('utf-8')
            server.send_id(cid, peer.Message(True, "GETNICK"))
            
        elif message.message_type == "MESSAGE ":
            for m in self.messages:
                if m[2] == data['message_id']:
                    return
        
            data = json.loads(message.payload.decode('utf-8'))
            
            self.messages.append(("MESSAGE", time.time(), data['sender_id'], data['message_id'], data['content']))
            self.on_app_message()
            
            for c in server.clients:
                if c.id not in data['closed']:
                    data['closed'].append(c.id)
                    
            server.broadcast(peer.Message(True, "MESSAGE", json.dumps(data).encode('utf-8')))
        
    def connected(self, server, client):
        self.server = server    
        server.broadcast(peer.Message(False, "QUERYALL", "{}:{}:{}:{}".format(*server.address, server.id, ''.join([random.choice(string.digits + string.ascii_letters) for _ in range(40)]), '#'.join([c.id for c in server.clients] + [server.id]))))