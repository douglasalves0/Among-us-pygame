from utils import constants, functions
import pygame, pygame_textinput
from screens.loadingConnection import loadingConnection
from screens.waitingLobby import waitingLobby

def showEnterGame(screen, name):

    manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 70)
    textInput = pygame_textinput.TextInputVisualizer(manager=manager, font_object=constants.calibriSmall)
    textInputWidth = 500

    serverSurface = constants.calibriBig.render("Please enter server", False, constants.color1)
    serverSurfaceWidth, serverSurfaceHeight = serverSurface.get_size()

    errorSurface = constants.calibriMedium.render("Server not found!", False, constants.color4)
    errorSurfaceWidth, errorSurfaceHeight = errorSurface.get_size()

    error = False

    while 1:

        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        for event in events:
            if event.type == pygame.QUIT:
                quit()

        textInput.update(events)

        if(keys[pygame.K_RETURN]):
            tcp = loadingConnection(screen, textInput.value)
            if(tcp == None):
                error = True
                continue
            waitingLobby(screen, tcp, name)

        screen.fill(constants.color3)
        pygame.draw.rect(screen, constants.white, pygame.Rect(functions.calcMid(constants.width,textInputWidth+60),180,textInputWidth+60,60))
        screen.blit(textInput.surface, (functions.calcMid(constants.width,textInputWidth),200))
        screen.blit(serverSurface, (functions.calcMid(constants.width, serverSurfaceWidth), 100))
        
        if(error):
            screen.blit(errorSurface, (functions.calcMid(constants.width, errorSurfaceWidth), 400))

        pygame.display.flip()

