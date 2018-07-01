import socket
import time
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #����socket (AF_INET:IPv4, AF_INET6:IPv6) (SOCK_STREAM:��������TCPЭ��)

s.bind(('127.0.0.1', 10021))                           #�󶨱���IP������˿�(>1024)

s.listen(1)                                            #�������ȴ����ӵ������ĿΪ1

print('Server is running...')                          
                               
def TCP(sock, addr):                                   #TCP�������˴����߼�
    
    print('Accept new connection from %s:%s.' %addr)   #�����µ���������

    while True:
        data = sock.recv(1024)                         #����������
        time.sleep(1)                                  #�ӳ�
        if not data or data.decode() == 'quit':        #�������Ϊ�ջ���'quit'�����˳�
            break
        sock.send(data.decode('utf-8').upper().encode())  #���ͱ�ɴ�д�������,���Ƚ���,�ٰ�utf-8����,  encode()��ʵ����encode('utf-8')

    sock.close()                                       #�ر�����
    print('Connection from %s:%s closed.' %addr)       

while True:
    
    sock, addr = s.accept()                            #����һ��������
    TCP(sock, addr)                                    #��������