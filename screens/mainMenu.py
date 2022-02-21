from utils import constants
import pygame, timeit

def showMainMenu():

    size = constants.width, constants.height
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("among us")

    lastTime = timeit.default_timer()

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        now = timeit.default_timer()
        fps = 1/(now-lastTime)
        lastTime = now
        fpsSurface = constants.calibri.render(f"FPS: {int(fps)}", False, constants.color1)


        screen.fill(constants.color3)
        screen.blit(fpsSurface, (50,400))
        pygame.display.flip()