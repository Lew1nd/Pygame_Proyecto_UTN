import pygame
from Colors import *
'''
pygame.init()

infoObject = pygame.display.Info()
pygame.display.set_mode((infoObject.current_w - 100, infoObject.current_h - 100))

flag = True
while flag:

    event_game = pygame.event.get()
    for event in event_game:
        if event.type == pygame.QUIT:
            print("Juego cerrado")
            flag = False

'''
'''
-----------------------
'''
pygame.quit()
import pygame.mixer as mixer
#from colores import *
#from config import *

def iniciar_pantalla_principal():
    datos_rectangulo = [0, 0, 200, 100]
    rectangulo_rojo = pygame.Rect(datos_rectangulo)
    imagen_largo = 800
    imagen_alto = 600
    datos_circulo = [700, 500]

    imagen = pygame.image.load('assets/gato.jpg')
    imagen = pygame.transform.scale(imagen, (imagen_largo, imagen_alto))
    rectangulo_imagen = imagen.get_rect()

    return rectangulo_rojo, rectangulo_imagen, imagen, datos_circulo

def iniciar_pantalla_secundaria():
    datos_circulo = [700, 500]
    return datos_circulo

def mostrar_pantalla_principal(rectangulo_rojo, rectangulo_imagen, imagen, datos_circulo):
    pantalla.fill(BLUE)

    pantalla.blit(imagen, rectangulo_imagen)

    pygame.draw.rect(pantalla, RED1, rectangulo_rojo)
    pygame.draw.circle(pantalla, GREEN, datos_circulo, 100)

def mostrar_pantalla_secundaria(datos_circulo):
    pantalla.fill(BURLYWOOD3)
    
    pygame.draw.circle(pantalla, CYAN2, datos_circulo, 50)

#region SETUP

pygame.init()
mixer.init()

# mixer.music.load('assets/y2mate.mp3')
# mixer.music.set_volume(0.1)

sonido = mixer.Sound('assets/y2mate.mp3')
sonido.set_volume(.1)

pantalla_actual = 1

#pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Grupo 1: Yo, Yo y Otra vez yo')

rectangulo_rojo, rectangulo_imagen, imagen, datos_circulo = iniciar_pantalla_principal()

pygame.display.set_icon(imagen)

direccion = 10
#endregion
#region Juego

# sonido.play()

pantalla_a_mostrar = pantalla

flag_seguir = False

texto = ""
flag_juego = True
flag_iniciada = True
while flag_juego:
    
    #region Eventos

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            print("Acá estoy")
            flag_juego = False
        elif evento.type == pygame.KEYDOWN:
            flag_iniciada = True
            if evento.key == pygame.K_DOWN:
                pantalla_actual += 1
            if evento.key == pygame.K_UP:
                pantalla_actual -= 1
            # if evento.key == pygame.K_BACKSPACE:
            #     texto = texto[0:-1]
            # else:
            #     texto += evento.unicode
            # print(texto)

        elif evento.type == pygame.MOUSEMOTION:
            mouse = list(evento.pos)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            flag_seguir = True
        elif evento.type == pygame.MOUSEBUTTONUP:
            flag_seguir = False
        

    #endregion
    
    #region Modificación de elementos
    
    if rectangulo_rojo.right < ANCHO_PANTALLA:
        rectangulo_rojo.left += direccion

    if flag_seguir:
        if mouse[0] > ANCHO_PANTALLA:
            mouse[0] = ANCHO_PANTALLA
        if mouse[1] > ALTO_PANTALLA:
            mouse[1] = ALTO_PANTALLA
        if mouse[0] < 0:
            mouse[0] = 0
        if mouse[1] < 0:
            mouse[1] = 0
        datos_circulo[0] = mouse[0]
        datos_circulo[1] = mouse[1]
    #endregion

    #region Dibujo de elementos
    if pantalla_actual == 1:
        if flag_iniciada:
            rectangulo_rojo, rectangulo_imagen, imagen, datos_circulo = iniciar_pantalla_principal()
            flag_iniciada = False
        mostrar_pantalla_principal(rectangulo_rojo, rectangulo_imagen, imagen, datos_circulo)
    elif pantalla_actual == 2:
        if flag_iniciada:
            datos_circulo = iniciar_pantalla_secundaria()
            flag_iniciada = False
        mostrar_pantalla_secundaria(datos_circulo)
    #endregion

    #region Muestra de pantalla

    pygame.display.flip()

    #endregion

#endregion
pygame.quit()

'''
#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
def funcion_gato_boton():
    print("Hola, soy el gato boton")
def funcion_gato_boton2():
    print("Hola, soy el gato boton 2")
def funcion_gato_boton3():
    print("Hola, soy el gato boton 3")

pygame.init()

lista_botones = [{"superficie" : pygame.transform.scale(pygame.image.load('assets/gatoboton.jpg'), (200, 200)),
                 "rect_pos" : pygame.Rect(0, 0, 200, 200),
                 "funcion" : funcion_gato_boton},
                 {"superficie" : pygame.transform.scale(pygame.image.load('assets/gatoboton2.jpg'), (200, 200)),
                 "rect_pos" : pygame.Rect(200, 200, 200, 200),
                 "funcion" : funcion_gato_boton2},
                 {"superficie" : pygame.transform.scale(pygame.image.load('assets/gatoboton3.jpg'), (200, 200)),
                 "rect_pos" : pygame.Rect(400, 400, 200, 200),
                 "funcion" : funcion_gato_boton3}]


pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Objetos de pygame como diccionarios')

flag_click = False
flag_juego = True
while flag_juego:
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_juego = False
        elif evento.type == pygame.MOUSEMOTION:
            mouse = list(evento.pos)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            flag_click = True
            
    if flag_click:
        for boton in lista_botones:
            if boton["rect_pos"].collidepoint(mouse[0], mouse[1]):
                boton["funcion"]()

