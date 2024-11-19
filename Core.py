import pygame
from Colors import *
from MenuConfig import *
import StaticFunctions

pygame.init()
game_running = True
StaticFunctions.current_screen = "Menu"

#region Class
menu_screen = Menu()
score_screen = Scoreboard()
options_screen = Options()
difficulty_screen = Difficulty()

#endregion

#region Update
while game_running:
    if StaticFunctions.current_screen == "Menu":
        game_running = menu_screen.init_menu()
    elif StaticFunctions.current_screen == "ScoreBoard":
        game_running = score_screen.init_scoreboard()
    elif StaticFunctions.current_screen == "Options":
        game_running = options_screen.init_options()
    elif StaticFunctions.current_screen == "Difficulty":
        game_running = difficulty_screen.init_difficulty()
    
    pygame.display.flip()
#endregion

pygame.quit()