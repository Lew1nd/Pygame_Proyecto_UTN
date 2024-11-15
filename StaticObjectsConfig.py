'''
Aquí estarán las funciones y objetos que pueden estar presenten en varias pantallas a la vez
'''
import pygame

def iniciar_pantalla():
    '''
    Función que inicializa una pantalla de juego.\n
    No recibe nada.\n
    Devuelve la resolución de la pantalla.
    '''
    pantalla = pygame.display.set_mode((1280,800))
    return pantalla