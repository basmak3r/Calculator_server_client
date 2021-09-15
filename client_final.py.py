from _thread import *
import threading
import socket
import sys

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',1025))
print("Client")



def receive():
    while(True):
        msg2=sock.recv(1024)
        print('Message From Server :',msg2.decode())
        if(msg2.decode()=="exit"):
            break
            


    

def send():
    while(True):
        msg1=input()
        sock.send(msg1.encode())
        if(msg1=="exit"):
            break


th1=threading.Thread(target=send)
th1.start()

th2=threading.Thread(target=receive)
th2.start()

th1.join()
th2.join()

sock.close()