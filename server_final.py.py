from _thread import *
import threading
import socket



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1025))
s.listen(5)
con,addr = s.accept()


def send():
    while(True):
        m1=input()
        con.send(m1.encode())
        if(m1=="exit"):
            break
        



def receive():
    while(True):
        m2=con.recv(1024)
    
        print('Message From Client :',m2.decode())
        if(m2.decode()=="exit"):
            break

        

print("Server")

th1=threading.Thread(target=send)
th1.start()

th2=threading.Thread(target=receive)
th2.start()

th1.join()
th2.join()
s.close()
