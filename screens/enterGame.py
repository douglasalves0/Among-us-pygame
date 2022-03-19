from utils import constants, functions
import pygame, pygame_textinput

def showEnterGame(screen):

    manager = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 70)
    textInput = pygame_textinput.TextInputVisualizer(manager=manager, font_object=constants.calibriSmall)
    textInputWidth = 500

    serverSurface = constants.calibriBig.render("Please enter server", False, constants.color1)
    serverSurfaceWidth, serverSurfaceHeight = serverSurface.get_size()

    while 1:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                quit()

        textInput.update(events)

        if(pygame.key.get_pressed()[pygame.K_RETURN]):
            print("conexão concluída")
            quit()
            

        screen.fill(constants.color3)
        pygame.draw.rect(screen, constants.white, pygame.Rect(functions.calcMid(constants.width,textInputWidth+60),180,textInputWidth+60,60))
        screen.blit(textInput.surface, (functions.calcMid(constants.width,textInputWidth),200))
        screen.blit(serverSurface, (functions.calcMid(constants.width, serverSurfaceWidth), 100))
        pygame.display.flip()

