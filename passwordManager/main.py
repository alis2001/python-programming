from cryptography.fernet import  Fernet #for text encryption

'''
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFIle:
        keyFIle.write(key)
'''

def loadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = loadKey()
fer = Fernet(key)



def add():
    name = input("Account Name: ")
    password = input("Password: ")
    with open('password.txt', 'a') as f: #with closes the file automatically
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|') #returns a list form data
            print("user : ", user, "| password : ", fer.decrypt(passw.encode()).decode())



while True:
    mode = input("Would you like to add a new password or view existing ones? (add/view) ? press q to quit !")
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Mode!")
        continue

