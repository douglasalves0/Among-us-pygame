from utils import constants, functions
import pygame, pygame_textinput
import socket

def loadingConnection(screen, ipPort):#Return connection, None if not connected

    serverSurface = constants.calibriBig.render("Connecting...", False, constants.color1)
    serverSurfaceWidth, serverSurfaceHeight = serverSurface.get_size()

    screen.fill(constants.color3)
    screen.blit(serverSurface, (functions.calcMid(constants.width, serverSurfaceWidth), constants.height//2))
    pygame.display.flip()

    connectList = ipPort.split(":")

    if(len(connectList) != 2):
        return None

    try:
        connectTuple = (connectList[0], int(connectList[1]))
    except:
        return None

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        tcp.connect(connectTuple)
    except:
        return None

    return tcp
