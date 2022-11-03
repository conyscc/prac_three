#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(('127.0.0.1', 1234))
    print('Connection is clear!')
    msg = input()
    sock.send(msg.encode('utf-8'))
    print('Message', msg, 'is send!')
    data = sock.recv(1024)
    sock.close()
    print(data)
    print('Connection is closed!')

