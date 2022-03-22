from connection.data import playerData
import json
import socket

def communicate(connection, client):

    while(1):

        try:

            print("esperando pacote")
            data = json.loads(connection.recv(2048).decode())
            print("pacote chegou")
            playerId = data["id"]

            print("CHEGOU")
            print(playerData)
            print("PASSOu")

            playerIndex = findById(playerData, playerId)

            if(playerIndex != -1):
                playerData["data"][playerIndex] = data
        
            print("enviando pacote")
            connection.send(json.dumps(playerData).encode())
            print("pacote enviado")

            print(f"data.playerData guarda {playerData}")

        except Exception as e:
            print(e)
            print(f"Disconnected from player {playerId}")
            connection.shutdown(socket.SHUT_RDWR)
            connection.close()
            break



def thereIsLeader(playerData):
    for player in playerData["data"]:
        if(player["isLeader"]):
            return True
    return False


def findById(playerData, id):
    for i in range(len(playerData["data"])):
        if(playerData["data"][i]["id"] == id):
            return i
    return -1
