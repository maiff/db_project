import socket
import sys

HOST = 'localhost'
PORT = 50507

def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    # print(s.recv(1024).decode())
    while 1:
        data = input('>>>')
        print(data)
        if data=='': continue;
        s.send(bytearray(data, 'utf-8'))
        print(s.recv(1024).decode())
        if data == 'exit':
            break
    s.close()


if __name__ == '__main__':
    socket_client()
