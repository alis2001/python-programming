from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

HOST = 'localhost'
PORT = 5500
BUFSIZ = 512
ADDR = (HOST, PORT)
maxConnections = 10

persons = []
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)

def broadcast(msg, name):
    """
    send new messages to all clients
    :param msg: bytes["utf8"]
    :param name: str
    :return:
    """
    for person in persons:
        client = person.client
        client.send(bytes(name, "utf8") + msg)

def clientCommunication(person):
    """
    thread to handle messages from clients
    :param client: Person
    :return: non
    """
    client = person.client
    #get person's name
    name = client.recv(BUFSIZ).decode("utf8")
    person.setName(name)
    msg = bytes(f"{name} has joined the chat!", "utf8")
    broadcast(msg, "") #welcome message

    while True:
        try:
            msg = client.recv(BUFSIZ)
            if msg != bytes("{quit}", "utf8"):
                client.close()
                persons.remove(person)
                broadcast(f"{name} has left the chat...", "")
                print(f"[DISCONNECTED] {name} disconnected")
                break
            else:
                broadcast(msg, name)
                print(f"{name}: ", msg.decode("utf8"))
        except Exception as e:
            print("[EXCEPTION]", e)
            break


def waitForConnection():
    """ wait for others to connect and start a new thread once connected """
    run = True
    while run:
        try:
            client, addr = server.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=clientCommunication, args=(person,)).start()
        except Exception as e:
            print("[CONNECTION]", e)
            run = False

    print("SERVER CRASHED")



if __name__ == "__main__":
    server.listen(maxConnections)
    print("[STARTED] waiting for connections ...")
    acceptThread = Thread(target=waitForConnection)
    acceptThread.start()
    acceptThread.join()
    server.close()
