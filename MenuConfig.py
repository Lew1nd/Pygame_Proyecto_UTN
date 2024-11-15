'''
Aquí estará todo lo relacionado a la pantalla de menú
'''
import pygame
from StaticFunctions import *
from Colors import *

button_start = [500, 250,250,100]#Posición x, posición Y, Largo, alto
button_score = [500, 450,250,100]
button_exit = [500,650,250,100]

menu_buttons = {'Start': button_start,
                'Score': button_score,
                'Exit': button_exit}

pantalla = iniciar_pantalla()
def init_menu():
    start_button = generar_rectangulo(menu_buttons['Start'])
    score_button = generar_rectangulo(menu_buttons['Score'])
    exit_button = generar_rectangulo(menu_buttons['Exit'])

    event_game = pygame.event.get()

    for event in event_game:#Eventos
        if event.type == pygame.QUIT:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Evento generado al presionar el click izquierdo
            if start_button.collidepoint(pygame.mouse.get_pos()):#Llama al evento cuando se presione button_start
                pantalla.fill(RED1)
            elif exit_button.collidepoint(pygame.mouse.get_pos()):
                print("Juego cerrado")
                return False

    pygame.draw.rect(pantalla, GREEN, start_button)
    pygame.draw.rect(pantalla, RED1, exit_button)
    return True