import socket

HOST = "localhost"
PORT = 35001


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.bind((HOST, PORT))

sock.listen(1)

conn, addr = sock.accept()

print "connected to ", addr

conn.sendall('Hello')


while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    print data

#close socket
conn.close()