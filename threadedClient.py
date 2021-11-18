import socket

sock = socket.socket()
sock.setblocking(1)

print('Подключение пользователя: ')
sock.connect(('127.0.0.5', 7070))

while True:
    print('Сообщение("exit" остановки сервера): ')
    inp = input()
    m=inp.encode()
    sock.send(m)
    if inp == 'exit':
        break
    m = sock.recv(1024)
    print(f'Принято сообщение от сервера: ',m.decode())

print('Остановка сервера')
sock.close()
