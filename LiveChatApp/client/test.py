from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
#global constants
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512

messages = []

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(ADDR)

def receiveMessages():
    """
    receive messages from server and then return
    :return:
    """
    while True:
        try:
            msg = clientSocket.recv(BUFSIZ)
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]", e)
            break
def sendMessage(msg):
    """
    send messages from server
    :param msg: str
    :return: non
    """
    clientSocket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        clientSocket.close()

receiveThread = Thread(target=receiveMessages)
receiveThread.start()

sendMessage("Ali")
time.sleep(10)
sendMessage("hello")
time.sleep(2)
sendMessage("{quit}")
