import socket

HOST = "127.0.0.1"
PORT = 35001


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.connect((HOST, PORT))

print "received from server: ", sock.recv(1024)

while True:
    inputVar = raw_input("Enter a message to send: ")

    sock.sendall(inputVar)

    recData = sock.recv(1024)
    print "received from server: ", recData
