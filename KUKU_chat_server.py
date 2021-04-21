import threading
import socket

s= socket.socket()
ip="192.168.43.140"
port=1234
s.bind((ip,port))
s.listen()
c,addr=s.accept()
sender_ip=str(addr[0])

print("/n/t/t/t/t/tWELCOME\n")
print("connected successfully...")

s.listen()
def send():
    while True:
      data=input("\n\t\t\t\t\t\t<<<: ")
      data=data.encode()
      c.send(data)


def recv():
    while True:
      data=c.recv(1024)
      data=data.decode()
      print("\n\t"+ip+":>>> "+data)

receive_thread=threading.Thread(target=recv)
send_thread=threading.Thread(target=send)

receive_thread.start()
send_thread.start()
s.close()	
