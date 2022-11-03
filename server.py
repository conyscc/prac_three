#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(4)
    print('--Conecting to client--')
    conn, addr = sock.accept()
    data = conn.recv(1024).decode('utf-8')
    print('Connection is clear!', addr[0], ':', addr[1])
    msg = ''
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        conn.send(data)
    print(msg)
    answer = input()
    cont=answer.encode('utf-8')
    conn.send(cont)
    print('Connection is closed!')
    conn.close()

