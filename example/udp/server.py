import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #����һ��socket,SOCK_DGRAM��ʾUDP

s.bind(('127.0.0.1', 10021))                         #��IP��ַ���˿�

print('Bound UDP on 10021...')

while True:                                          
    data, addr = s.recvfrom(1024)   #������ݺͿͻ��˵ĵ�ַ��˿�,һ��������1024�ֽ�
    print('Received from %s:%s.' % addr)
    s.sendto(data.decode('utf-8').upper().encode(), addr)#�����ݱ�ɴ�д�ͻؿͻ���

#���ر�socket