from utils import constants, functions
from var import playerVar
from connection.functions import response
import pygame, pygame_textinput
import socket
import threading
import json

def waitingLobby(screen, tcp, name):

	serverSurface = constants.calibriBig.render("CONECTADO COM SUCESSO", False, constants.color1)
	serverSurfaceWidth, serverSurfaceHeight = serverSurface.get_size()

	tcp.send(name.encode())
	data = json.loads(tcp.recv(1024).decode())

	playerVar.playerId = data["id"]
	playerVar.isLeader = data["isLeader"]

	t = threading.Thread(target=response, args=[tcp])
	t.start()

	while 1:

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				quit()

		screen.fill(constants.color3)
		screen.blit(serverSurface, (functions.calcMid(constants.width, serverSurfaceWidth), 200))
		pygame.display.flip()
