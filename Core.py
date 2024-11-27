import pygame
from Colors import *
from MenuConfig import *
import StaticFunctions

pygame.init()
fps = pygame.time.Clock()
game_running = True
StaticFunctions.current_screen = "Menu"

#region Class
#menu_screen = Menu()
#score_screen = Scoreboard()
#options_screen = Options()
#difficulty_screen = Difficulty()
#question_manager = QuestionManager()

dict_menus = {'Menu': Menu(),
              'ScoreBoard': Scoreboard(),
              'Options': Options(),
              'Difficulty': Difficulty(),
              'QuestionManager': QuestionManager(),
              'Categories': Categories(),
              'Game': Game(),
              'FinalScreen': FinalScreen()  # Instancia de la pantalla final
              }


#endregion

StaticFunctions.cargar_datos(StaticFunctions.player_datapath, "Player")

#region Update
while game_running:
    match StaticFunctions.current_screen:
        case "Menu": game_running = dict_menus['Menu'].init_menu()
        case "ScoreBoard": game_running = dict_menus['ScoreBoard'].init_scoreboard()
        case "Options": game_running = dict_menus['Options'].init_options()
        case "Difficulty": game_running = dict_menus['Difficulty'].init_difficulty()
        case "QuestionManager": game_running = dict_menus['QuestionManager'].init_question_manager()
        case "Categories": game_running = dict_menus['Categories'].init_categories()
        case "Game": game_running = dict_menus['Game'].init_game()
        case "FinalScreen": game_running = dict_menus['FinalScreen'].init_final_screen()

    '''
    if StaticFunctions.current_screen == "Menu":
        game_running = menu_screen.init_menu()
    elif StaticFunctions.current_screen == "ScoreBoard":
        game_running = score_screen.init_scoreboard()
    elif StaticFunctions.current_screen == "Options":
        game_running = options_screen.init_options()
    elif StaticFunctions.current_screen == "Difficulty":
        game_running = difficulty_screen.init_difficulty()
    elif StaticFunctions.current_screen == "QuestionManager":
        game_running = question_manager.init_question()
    '''
    #print(f"FPS actuales: {fps.get_fps()}")
    
    pygame.display.flip()
#endregion
fps.tick(60)
pygame.quit()