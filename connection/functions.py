import json
import socket
from var import playerVar

def response(tcp):

    while(1):

        print("Enviando pacote")

        tcp.send(json.dumps({
            "id": playerVar.playerId,
            "isDead": playerVar.isDead,
            "isLeader": playerVar.isLeader,
            "x": playerVar.x,
            "y": playerVar.y,
            "deadX": playerVar.deadX,
            "deadY": playerVar.deadY,
        }).encode())

        print("pacote enviado !")

        data = json.loads(tcp.recv(2048).decode())
        playerVar.data = data
        