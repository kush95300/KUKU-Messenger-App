
# coding: utf-8

# In[ ]:


import threading
import socket


s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="192.168.43.185"
port=1234

s.connect((ip,port))
print("\n\t\t\t\t\tWELCOME\n")
print("connected successfully...")

def csend():
    while True:
      data=input("\n\t\t\t\t\t\t<<<: ")
      data=data.encode()
      s.send(data)


def crecv():
    while True:
      data=s.recv(1024)
      data=data.decode()
      print("\n\t"+ip+":>>> "+data)

receive_thread=threading.Thread(target = crecv)
send_thread=threading.Thread(target = csend)

receive_thread.start()
send_thread.start()


