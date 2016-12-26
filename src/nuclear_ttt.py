# i = j collusion: ^stake + 1000
# i -1 dev: stake/i-1
#

### BROADCAST (optional)
# Enter broadcast message
# [OUT] Publish message to server. For each client publish message
# [IN] Take in outstanding messages and print

### PRIVATE message
# Enter message
# Enter CAESAR encryption key and dir
# Create encrypted message w/ key in message
# [OUT] Publish message and instruction to server
# [IN] Rec take in message
# Rec decrypt message and print on local

### Football
# Fire Code Keygen
# Enter Code Keygen
# Process Code
# [OUT] Publish fire code to server
# [IN] Take firecode in from server
# Create Missle object
# Run missle until detonation (turn-based)

### Payment
# Create payment requeust
# [OUT] Publish payment code to server
# [IN] Take in new pay requeust
# Add credits

import socket
import time
import threading

tLock = threading.Lock()
exit = False


class Player(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.cash = 2000

    def init_fire(self):
        target = input("Enter: ")
        fire_code = "[F] ORIGIN |" + name + "| TRGTL |" + target + "| ETA 10 turns"
        return fire_code

    def init_pmt(self):
        target = input("Enter target name: ")
        amt = input("Input amt: ")
        pmt_code = "[P] ORIGIN |" + name + "| TRGTL |" + target + "| AMT " + amt
        return pmt_code

    def sendTransmission(self):
        target = input("Enter target name: ")
        msg = input("Message: ")

        # ENCRYPT W/ CAESAR CIPHER HERE

        msg_code = "[X] ORIGIN |" + name + "| TRGTL |" + target + "| MSSG |" + msg
        return msg_code

    def inject(self, funds):
        self.cash = self.cash + funds

    def chat(self, message):
        pass

class Proj(object):
    def __init__(self, launch_time, origin, trgt):
        self.launch_time = launch_time

    def det(self):
        # if now - launch = 10 mins, DETONATE
        # run probability detonation "[F] ORIGIN |<name>| TRGT |<target>| IMPACT |<success>|"
        pass

class Space(object):
    def __init__(self, players):
        self.players = players
        self.air = []

    def addKin(self, mssl):
        self.air.append(mssl)

    def raise_stakes(self):
        # for all players raise stakes by 1000
        pass

def receiving(name, sock):
    while not exit:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data).replace("b", ""))
        except:
            pass
        finally:
            tLock.release()

def sendMessage(instruction_code):
    tLock = threading.Lock()
    exit = False

    host = '127.0.0.1' # your ip address
    port = 0

    server = ('127.0.0.1', 80) #server ip

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    s.setblocking(0)

    rT = threading.Thread(target=receiving, args=["RecvThread", s])
    rT.start()
    # alias = input("Name: ")
    message = instruction_code

    s.sendto(str.encode(message.replace("b'","")), server)
    tLock.acquire()
    # message = input(alias + ":   ")
    tLock.release()
    time.sleep(0.2)

    exit = True
    #rT.join()
    s.close()

def recMessage():
    pass


entry = False

while(entry is False):
    name = input("Name: ")
    user = Player(name)
    entry = True

exit = False

while(exit is False):
    print("[1] Broadcast")
    print("[2] Private Message")
    print("[3] Football")
    print("[4] Payment")
    print("[Q] Exit")
    print("")

    action = input("$ ")

    if(action is "2"): sendMessage(user.sendTransmission())
    if(action is "3"): sendMessage(user.init_fire())
    if(action is "4"): sendMessage(user.init_pmt())
    if(action is "q"):
        exit = True
