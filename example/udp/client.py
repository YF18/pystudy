import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
 
addr = ('127.0.0.1', 10021)       #�������˵�ַ

while True:
    data = input('������Ҫ���������:') #�������
    if not data or data == 'quit':
        break
    s.sendto(data.encode(), addr)    #���͵������
    recvdata, addr = s.recvfrom(1024)  #���շ������˷���������
    print(recvdata.decode('utf-8'))    #�����ӡ

s.close()            #�ر�socket