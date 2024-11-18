'''
Aquí estarán las funciones y objetos que pueden estar presentes en varias pantallas a la vez
'''
import pygame
current_screen = ""
change_screen_flag = True
    
def iniciar_pantalla():
    '''
    Función que inicializa una pantalla de juego.\n
    No recibe nada.\n
    Devuelve la resolución de la pantalla.
    '''
    pantalla = pygame.display.set_mode((1280,800))
    return pantalla

def generar_rectangulo(surface, color, button_dimensions: list):
    '''
    Genera un objeto de tipo rectángulo.\n
    Recibe una lista con las dimensiones del rectángulo y su posición, además del color y la superficie (pantalla actual).\n
    Devuelve el objeto.
    '''
    rectangulo = pygame.Rect(button_dimensions)
    boton = pygame.draw.rect(surface, color, rectangulo)
    return boton

def dibujar_texto(surface , string: str, font_size: int, color, position: list, font = "Arial"):
    '''
    Genera un texto y lo muestra en pantalla.\n
    Recibe la pantalla, la cadena, el tamaño de la fuente, un color, la posición en pantalla y una fuente (por defecto es Arial).\n
    Devuelve el objeto
    '''
    text_font = pygame.font.SysFont(font, font_size)#Se guarda la fuente que se utilizará en el texto
    text_txt = text_font.render(string, True, color)#Posteriormente, se crea el texto
    text_object = surface.blit(text_txt, position)#Y luego se muestra en la pantalla
    return text_object

def dibujar_imagen(surface, path: str, imagen_dimensions: list):
    '''
    Dibuja una imagen.\n
    Recibe la pantalla, la ubicación del archivo y las dimensiones de la imagen (tamaño y ubicación en pantalla).\n
    Devuelve el objeto 
    '''
    img = pygame.image.load(path)
    img_object = pygame.transform.scale(img, (imagen_dimensions[2], imagen_dimensions[3]))
    surface.blit(img_object, (imagen_dimensions[0], imagen_dimensions[1]))
    return img_object

def cambiar_pantalla(name: str) -> str:
    print("Pantalla cambiada a", name)
    return name

def iniciar_musica(volume: float, loops: int, path: str):
    '''
    Inicia la música.\n
    Recibe el volumen, la cantidad de veces que se va a repetir (loop) y la ubicación del archivo en la carpeta (path).\n
    No devuelve nada
    '''
    pygame.mixer.music.stop()#Para la musica
    pygame.mixer.music.load(path)#Carga la musica para el menu
    pygame.mixer.music.set_volume(volume)#Establece el volumen
    pygame.mixer.music.play(loops)#Veces que se repetirá (-1 para infinitas veces)
