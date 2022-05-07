import socket
import threading

#required CONSTANTS
HEADER = 64 #bytes each msg carries
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #LOCAL host
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECTMESSAGE = "!DISCONNECTED" #handling disconnection smoothly

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #what type of ip we accept
server.bind(ADDR) #this socket is binded

def handleClient(conn, addr): #handle new conn and comunication between client and server
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msgLength = conn.recv(HEADER).decode(FORMAT) #how many bytes we want to receive we will not pass it till we receive a mesg from client
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            if msg == DISCONNECTMESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message received".encode(FORMAT))
    conn.close()
def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn , addr = server.accept() #this waits for a new conn to absorb ip address and port
        thread = threading.Thread(target=handleClient, args=(conn, addr)) #we passing new conn to handleClient
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #how many threads are active in this process but there is only one thread so we subtract by one

print("[STARTING] server is starting")
start()
