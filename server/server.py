from connection import data
from connection.functions import communicate, thereIsLeader
import socket
import threading
import random
import json

HOST = "localhost"
PORT = None

try:
	PORT = int(input("ENTER THE DESIRED PORT TO RUN THE SERVER: "))
except:
	print("Please choice a number to the application port!!")
	quit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)

try:
	tcp.bind(origem)
except:
	print("The chosen port was already being used!!")
	quit()

tcp.listen(20)
tcp.settimeout(10)
print(f"SUCCESSFULLY CONNECTED TO LOCALHOST:{PORT}")

while(1):

    started = False
    idCounter = 0

    while(not started):
		
        try:
            connection, client = tcp.accept()
            name = connection.recv(1024).decode()
        except Exception as e:
            continue

        if(name.startswith("SSH") or name == ""):
            print("REJECTED NGROK CONNECTION!!")
            continue
	
        isLeader = False
        if(not thereIsLeader(data.playerData)):
            isLeader = True

        pack = {
            "id": idCounter,
            "isDead": False,
            "isLeader": isLeader,
            "x": 0,
            "y": 0,
            "deadX": 0,
            "deadY": 0
        }
        
        try:
            connection.send(json.dumps(pack).encode())
        except Exception as e:
            print(e)
            continue

        data.playerData["data"].append(pack)

        t = threading.Thread(target=communicate, args=[connection, client])
        t.start()

        idCounter+=1
        print(f"CONNECTED TO USER {name}!!")