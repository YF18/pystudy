import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #����һ��socket

s.connect(('127.0.0.1', 10021))                       #��������

while True:                                           #���ܶ������

    data = input('������Ҫ���͵����ݣ�')                 #��������

    if data == 'quit':                                #���Ϊ'quit',���˳�
        break

    s.send(data.encode())                             #���ͱ���������

    print(s.recv(1024).decode('utf-8'))               #��ӡ���յ��Ĵ�д����

s.send(b'quit')                                       #��������

s.close()                                             #�ر�socket