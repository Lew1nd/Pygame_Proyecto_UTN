import pygame
from Colors import *
from MenuConfig import *
from StaticFunctions import *

pygame.init()
game_running = True

while game_running:
    game_running = init_menu()

    pygame.display.flip()

pygame.quit()

