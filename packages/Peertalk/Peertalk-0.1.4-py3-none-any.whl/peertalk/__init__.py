import peertable as peer
import threading
import queue
import json
import random
import string
import wx
import time


class ChatApp(peer.PeerApplication):
    def __init__(self, nickname):
        self.nickname = nickname
        self.messages = queue.Queue()
        self.all_messages = []
        self.nicknames = {}
        self.users = []
        self.server = None

    def on_app_message(self):
        pass
        
    def send_message(self, msg):
        if self.server is None:
            return
    
        mid = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)])
        
        t = time.time()
        self.messages.put(("MESSAGE", t, self.server.id, mid, msg))
        self.all_messages.append(("MESSAGE", t, self.server.id, mid, msg))
        self.on_app_message()
        
        self.server.broadcast(peer.Message(True, "MESSAGE", json.dumps({
            'sender_id': self.server.id,
            'message_id': mid,
            'content': msg,
            'closed': [self.server.id]
        })))
        
    def send_privmsg_id(self, id, msg):
        if self.server is None:
            return
    
        mid = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)])
        
        t = time.time()
        self.messages.put(("PMESSAGE", t, self.server.id, mid, msg))
        self.all_messages.append(("PMESSAGE", t, self.server.id, mid, msg))
        self.on_app_message()
        
        self.server.send_id(id, peer.Message(True, "PMESSAGE", json.dumps({
            'sender_id': self.server.id,
            'message_id': mid,
            'content': msg
        })))
        
    def quit(self):
        if self.server is None:
            return
            
        self.server.broadcast(peer.Message(True, "QUIT", "{}:{}:{}".format(self.server.id, ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)]), self.server.id)))
        
    def set_nick(self, nick):
        if self.server is None:
            return
    
        self.nickname = nick
        self.nicknames[self.server.id] = nick
        self.server.broadcast(peer.Message(True, "MYNAMEIS", "{}:{}:{}".format(self.server.id, ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)]), self.server.id)))
        
    def receive(self, server, client, message):
        print("> Got '{}' message from ID '{}'".format(message.message_type.rstrip(' '), client.id))
    
        if message.message_type == "GETNICK ":
            nid = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)])
            server.send_id(client.id, peer.Message(True, "MYNAMEIS", ':'.join([nid, self.nickname])))
            # client.disconnect() # would prevent too many clients from populating our lists
            
        elif message.message_type == "TPNAMEIS":
            nid, cid, old_nick, nick = message.payload.decode('utf-8').split(':')
            t = time.time()
            
            if cid == server.id or nid in [x[2] for x in self.all_messages if x[0] == "NICK" and t - x[1] < 20]:
                return
            
            if cid not in self.users:
                self.users.append(cid)
                
            self.messages.put(("NICK", t, nid, cid, old_nick or None, nick))
            self.all_messages.append(("NICK", t, nid, cid, old_nick or None, nick))
            self.on_app_message()
            self.nicknames[cid] = nick
            server.broadcast(peer.Message(True, "TPNAMEIS", ":".join([nid, cid, old_nick, nick])))
        
        elif message.message_type == "MYNAMEIS":
            nid, nick = message.payload.decode('utf-8').split(':')
            
            if client.id in self.nicknames and nick == self.nicknames[client.id]:
                return
                    
            self.messages.put(("NICK", time.time(), nid, client.id, self.nicknames.get(client.id, None), nick))
            self.all_messages.append(("NICK", time.time(), nid, client.id, self.nicknames.get(client.id, None), nick))
            self.on_app_message()
            
            if client.id in self.nicknames:
                server.broadcast(peer.Message(True, "TPNAMEIS", ":".join([nid, client.id, self.nicknames[client.id], nick])))
                
            else:
                server.broadcast(peer.Message(True, "TPNAMEIS", ":".join([nid, client.id, "", nick])))
                
            self.nicknames[client.id] = nick
            
            if client.id not in self.users:
                self.users.append(client.id)
                
            print("Client {} identified as: {}".format(client.id, self.nicknames[client.id]))
                
        elif message.message_type == "QUIT    ":
            quitter, quit_id, closed = message.payload.decode('utf-8').split(':')
            closed = closed.split('#')
            
            t = time.time()
            
            if quit_id in [x[3] for x in self.all_messages if x[0] == "QUIT" and t - x[1] < 20]:
                return
            
            self.messages.put(("QUIT", time.time(), quit_id, quitter))
            self.all_messages.append(("QUIT", time.time(), quit_id, quitter))
            self.on_app_message()
            
            for c in server.clients:
                if c.id == quitter:
                    c.disconnect()
            
                elif c.id not in closed:
                    closed.append(c.id)
                    
            server.broadcast(peer.Message(True, "QUIT", "{}:{}:{}".format(quitter, quit_id, '#'.join(closed))))
    
        elif message.message_type == "JOIN    ":
            joiner, join_id, closed = message.payload.decode('utf-8').split(':')
            closed = closed.split('#')
            
            t = time.time()
            
            if join_id in [x[2] for x in self.all_messages if x[0] == "JOIN" and t - x[1] < 20] or joiner == self.server.id:
                return
            
            self.messages.put(("JOIN", time.time(), join_id, joiner))
            self.all_messages.append(("JOIN", time.time(), join_id, joiner))
            self.on_app_message()
            
            for c in server.clients:
                if c.id == joiner:
                    c.disconnect()
            
                elif c.id not in closed and c.id is not None:
                    closed.append(c.id)
                    
            server.broadcast(peer.Message(True, "JOIN", "{}:{}:{}".format(joiner, join_id, '#'.join(closed))))
    
        elif message.message_type == "__QUERYR":
            cid = message.payload.decode('utf-8')
            server.send_id(cid, peer.Message(True, "GETNICK"))
            
        elif message.message_type == "MESSAGE ":
            data = json.loads(message.payload.decode('utf-8'))
            t = time.time()
            
            for m in self.all_messages:
                if m[0] == "MESSAGE" and m[3] == data['message_id'] and t - m[1] < 20:
                    return
            
            self.messages.put(("MESSAGE", t, data['sender_id'], data['message_id'], data['content']))
            self.all_messages.append(("MESSAGE", t, data['sender_id'], data['message_id'], data['content']))
            self.on_app_message()
            
            for c in server.clients:
                if c.id not in data['closed']:
                    data['closed'].append(c.id)
                    
            server.broadcast(peer.Message(True, "MESSAGE", json.dumps(data).encode('utf-8')))
        
        elif message.message_type == "PMESSAGE":
            data = json.loads(message.payload.decode('utf-8'))
            self.messages.put(("PMESSAGE", t, data['sender_id'], data['message_id'], data['content']))
            self.all_messages.append(("PMESSAGE", t, data['sender_id'], data['message_id'], data['content']))
            self.on_app_message()
        
    def on_registered(self, server):
        self.server = server
        self.nicknames[self.server.id] = self.nickname
        server.broadcast(peer.Message(False, "QUERYALL", "{}:{}:{}:{}:{}".format(*server.address, server.id, ''.join([random.choice(string.digits + string.ascii_letters) for _ in range(40)]), '#'.join([c.id for c in server.clients if c and c.id] + [server.id]))))
        
    def connected(self, server, client):   
        # wait until client has identified
        def update():
            print("Identifying client {}...".format(client.id))
            
            while client.id is None:
                time.sleep(0.1)
        
            print("Labeling client {}...".format(client.id))
            jid = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(50)])
            self.messages.put(("JOIN", time.time(), jid, client.id))
            self.on_app_message()
            
            server.broadcast(peer.Message(True, 'JOIN', "{}:{}:{}".format(client.id, jid, self.server.id)))
            client.send(peer.Message(True, "GETNICK"))
            
        threading.Thread(target=update).start()