from utils import constants, functions
from screens import mainMenu
import pygame

pygame.init()

size = constants.width, constants.height
screen = pygame.display.set_mode(size)

pygame.display.set_caption("among us")

mainMenu.showMainMenu(screen)