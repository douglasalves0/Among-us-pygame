from screens.enterGame import showEnterGame
from utils import constants, functions
import pygame, timeit

def showMainMenu(screen, name):

    playButton = pygame.image.load("textures/buttons/mainMenu/play.png")
    playButtonWidth = playButton.get_width()
    playButtonHeight = playButton.get_height()
    playButton = pygame.transform.scale(pygame.image.load("textures/buttons/mainMenu/play.png"), (int(playButtonWidth/5), int(playButtonHeight/5)))

    pygame.mixer.music.load("audio/menu/menuSelection.mp3")

    lastTime = timeit.default_timer()
    isCollidingInPlayButtonInLastSprite = False

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        now = timeit.default_timer()
        fps = 1/(now-lastTime)
        lastTime = now
        fpsSurface = constants.calibriSmall.render(f"FPS: {int(fps)}", False, constants.color2)
        
        mousePosition = pygame.mouse.get_pos()
        playRect = playButton.get_rect()
        newPosition = (functions.calcMid(constants.width, playButton.get_width()), functions.calcMid(constants.height, playButton.get_height()))
        
        playRect.update(newPosition,(playButton.get_width(), playButton.get_height()))
        
        if(playRect.collidepoint(mousePosition)):
            if(pygame.mouse.get_pressed()[0]):
                showEnterGame(screen,name)
            if(not isCollidingInPlayButtonInLastSprite):
                playButton = pygame.transform.scale(pygame.image.load("textures/buttons/mainMenu/play.png"), (int(playButtonWidth/4.5), int(playButtonHeight/4.5)))
                pygame.mixer.music.play()
            isCollidingInPlayButtonInLastSprite = True
        else:
            if(isCollidingInPlayButtonInLastSprite):
                playButton = pygame.transform.scale(pygame.image.load("textures/buttons/mainMenu/play.png"), (int(playButtonWidth/5),   int(playButtonHeight/5)))
                pygame.mixer.music.play()
            isCollidingInPlayButtonInLastSprite = False

        screen.fill(constants.color3)
        screen.blit(fpsSurface, (10,430))
        screen.blit(playButton, newPosition)
        pygame.display.flip()

