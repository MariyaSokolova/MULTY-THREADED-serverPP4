import socket, sys, threading

def ThreadedServ(conn, addr):
    while True:
        print('Получено сообщение от пользователя: ')
        try:
            m = conn.recv(1024)
            print('Сообщение от пользователя ', addr, ': ', m.decode)
            print('Сообщение пользователю')
            conn.send(m)
        except (ConnectionResetError, ConnectionAbortedError):
            print('Отключение пользователя')
            raise

sys.tracebacklimit = 0
sock = socket.socket()
print('Запуск сервера')
sock.bind(('', 7070))
print('Прослушивание порта')
sock.listen(0)

while True:
    conn, addr = sock.accept()
    print("Подключение клиента: ",addr)
    serv=threading.Thread(target = ThreadedServ, args = (conn, addr), daemon = True)
    serv.start()

print('Прекращение работы сервера')
