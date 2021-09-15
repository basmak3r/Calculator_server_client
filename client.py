import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1025))
s.listen(5)
con,addr = s.accept()

while(True):
    msg2=con.recv(1024)
    msg2.decode()
    total = str(eval(msg2))
    con.send(total.encode())