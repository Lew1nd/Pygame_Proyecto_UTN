'''
Aquí estarán las funciones y objetos que pueden estar presentes en varias pantallas a la vez
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

def generar_rectangulo(button_dimensions: list):
    '''
    Genera un objeto de tipo rectángulo.\n
    Recibe una lista con las dimensiones del rectángulo, además de su posición.\n
    Devuelve el objeto.
    '''
    boton = pygame.Rect(button_dimensions)
    return boton