import socket

ip = '192.168.10.60'   # 문자열
port = 21              # 숫자

s = socket.socket()
s.connect((ip, port))
ans = s.recv(1024)
print(ans)


if 'vsFTPd 2.3.4' in str(ans):
    print(' ok back')
elif 'vsFTPd 3.0.3' in str(ans):
    print(' ok remote')
elif 'vsFTPd 2.0.5' in str(ans):
    print('deny')
else:
    print('fail - not vulunerable')