'''
Aquí estará todo lo relacionado a la pantalla de menú
'''
import pygame
import StaticFunctions
from Colors import *
#region Menu
class Menu():
    def __init__(self):
        self.screen_color = BLUEVIOLET

        self.button_start = [500, 250,250,100]#Posición x, posición Y, Largo, alto
        self.button_score = [500, 450,250,100]
        self.button_exit = [500,650,250,100]

        self.menu_buttons = {'Start': self.button_start,
                             'Score': self.button_score,
                             'Exit': self.button_exit}
    
    def init_menu(self):
        start_button = StaticFunctions.generar_rectangulo(self.menu_buttons['Start'])
        score_button = StaticFunctions.generar_rectangulo(self.menu_buttons['Score'])
        exit_button = StaticFunctions.generar_rectangulo(self.menu_buttons['Exit'])

        if StaticFunctions.change_screen_flag:
            self.menu = StaticFunctions.iniciar_pantalla()
            self.menu.fill(self.screen_color)
            StaticFunctions.change_screen_flag = False


        event_game = pygame.event.get()
        for event in event_game:#Eventos
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Evento generado al presionar el click izquierdo
                if start_button.collidepoint(pygame.mouse.get_pos()):#Llama al evento cuando se presione button_start
                    self.menu.fill(RED1)
                elif score_button.collidepoint(pygame.mouse.get_pos()):
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("ScoreBoard")
                    StaticFunctions.change_screen_flag = True

                elif exit_button.collidepoint(pygame.mouse.get_pos()):
                    print("Juego cerrado")
                    return False

        pygame.draw.rect(self.menu, GREEN, start_button)
        pygame.draw.rect(self.menu, YELLOW1, score_button)
        pygame.draw.rect(self.menu, RED1, exit_button)
        return True
#endregion
#region Score
class Scoreboard():
    def __init__(self):
        self.screen_color = GREEN1

        self.button_back = [500,650,250,100]

        self.score_buttons = {'Back': self.button_back}

        

    def init_scoreboard(self):
        back_button = StaticFunctions.generar_rectangulo(self.score_buttons['Back'])

        if StaticFunctions.change_screen_flag:
            self.score = StaticFunctions.iniciar_pantalla()
            self.score.fill(self.screen_color)
            StaticFunctions.change_screen_flag = False
        
        event_game = pygame.event.get()
        for event in event_game:
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Evento generado al presionar el click izquierdo
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Menu")
                    StaticFunctions.change_screen_flag = True



        pygame.draw.rect(self.score, RED1, back_button)
        return True
#endregion