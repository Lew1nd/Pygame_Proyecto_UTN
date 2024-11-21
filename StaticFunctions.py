'''
Aquí estarán las funciones y objetos que pueden estar presentes en varias pantallas a la vez
'''
import pygame
current_screen = ""
change_screen_flag = True
WIDTH, HEIGHT = 1280,800

#Atributos del jugador
lives = 3
time = 30
current_score = 0
score_gain_per_question = 1

#Gestionador de preguntas y respuestas
questions = ["Ingrese su pregunta aquí", 
             "Ingrese una posible respuesta aquí", 
             "Ingrese una posible respuesta aquí", 
             "Ingrese una posible respuesta aquí",
             "Ingrese una posible respuesta aquí",
             "Ingrese la respuesta correcta aquí"]#6

selected_category = "None"
selected_difficulty = "None"

def iniciar_pantalla():
    '''
    Función que inicializa una pantalla de juego.\n
    No recibe nada.\n
    Devuelve la resolución de la pantalla.
    '''
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
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

def dibujar_texto(surface , string: str, font_size: int, color, position: list, is_bold: bool, is_italic: bool ,font = "Arial"):
    '''
    Genera un texto y lo muestra en pantalla.\n
    Recibe la pantalla, la cadena, el tamaño de la fuente, un color, la posición en pantalla y una fuente (por defecto es Arial).\n
    Devuelve el objeto
    '''
    text_font = pygame.font.SysFont(font, font_size, is_bold, is_italic)#Se guarda la fuente que se utilizará en el texto
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
    return pygame.Rect(imagen_dimensions)

def cambiar_pantalla(name: str) -> str:
    '''
    Cambia la pantalla.\n
    Recibe el nombre de la pantalla como parámetro.\n
    Devuelve el nombre de la pantalla.\n
    '''
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


def entrada_texto(surface, color ,pygame_event, text, max_value: int, check_is_int: bool):
    '''
    Función encargada de añadir el nuevo caracter a la cadena.\n
    Recibe una pantalla (superficie), un color, el gestionador de eventos, una cadena de texto y un número entero que servirá para limitar el número máximo.\n
    Retorna la cadena.
    '''
    surface.blit(color, (0, 0))
    text = str(text)
    new_text = text + pygame_event.unicode
    if check_is_int:
        if comprobar_entero(new_text, max_value): return new_text 
    else:
        return new_text
    return text

def comprobar_entero(string: str, max_value: int):
    '''
    Comprueba si una cadena de string es de números enteros.\n
    Recibe la cadena y un valor máximo para limitar un valor máximo de enteros.\n
    Retorna True o False según sea el caso
    '''
    if string == "":
        return True
    if string.isnumeric():
        num = int(string)
        if num <= 0 or num > max_value:
            return False
        else:
            return True
    return False

def suprimir_texto(surface, color, event, value_selected: str):
    '''
    Elimina la cadena actual.\n
    Recibe la superficie de la pantalla, un color, el gestionador de eventos y una cadena.\n
    Retorna el texto
    '''
    surface.blit(color, (0, 0))
    if event.key == pygame.K_BACKSPACE:
        value_selected = value_selected[0:-1]
    return value_selected

def seleccionar_texto(text_list: list, selected_text: int):
        '''
        Permite establecer foco en una cadena de texto para permitir la escritura. Desactiva el foco de las demás cadenas existentes.\n
        Recibe un índice para una lista que posteriormente se utilizará para activar la casilla de texto correspondiente.\n
        No devuelve nada.
        '''
        text_list[:] = [False] * len(text_list)
        text_list[selected_text] = True

def texto_vacio(text_list: list, string: str, selected_text: int):
        '''
        Comprueba si el usuario dejó vacío el texto.
        Recibe la cadena, y el índice de la cadena de texto que se está modificando
        No devuelve nada
        '''
        if string == "": text_list[selected_text] = True
        else: text_list[selected_text] = False