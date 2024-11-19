'''
Aquí estará todo lo relacionado a las pantallas
'''
import pygame
import StaticFunctions
from Colors import *
#region Menú
class Menu():
    def __init__(self):
        self.menu = StaticFunctions.iniciar_pantalla()
        pygame.display.set_caption ("BGB")
        icono = pygame.image.load("archivos_multimedia/imagenes/icono_preguntados.png")#Carga el incono de la ventana
        StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu2.mp3")
        pygame.display.set_icon(icono)
        
        #Cargar la imagen del fondo
        self.fondo = pygame.image.load("archivos_multimedia/imagenes/menu_principal.png")
        self.fondo = pygame.transform.scale(self.fondo, self.menu.get_size())#Escala al tamaño de la pantalla

        #botones
        self.button_start = [470, 260, 355, 96]#Posición x, posición Y, Largo, alto
        self.button_score = [470, 370, 355, 96]
        self.button_options = [470, 487, 355, 96]
        self.button_exit = [470, 600, 355, 96]
        self.button_music = [1190, 10, 75, 75]



        #imagen muestra (temporal)
        self.imagen_1 = [0,0,500,500]

        self.muteado = False

    def init_menu(self):


        start_button = StaticFunctions.dibujar_imagen(self.menu,"archivos_multimedia/imagenes/boton_jugar.png" , self.button_start)
        score_button = StaticFunctions.dibujar_imagen(self.menu, "archivos_multimedia/imagenes/boton_score.png", self.button_score)
        music_button = StaticFunctions.dibujar_imagen(self.menu,"archivos_multimedia/imagenes/boton_musica.png", self.button_music)
        options_button = StaticFunctions.dibujar_imagen(self.menu, "archivos_multimedia/imagenes/boton_ajustes.png", self.button_options)
        exit_button = StaticFunctions.dibujar_imagen(self.menu, "archivos_multimedia/imagenes/boton_salir.png", self.button_exit)

        #img1 = StaticFunctions.dibujar_imagen(self.menu, "archivos_multimedia/imagenes/icono_preguntados.png", self.imagen_1)#imagen de preguntados
        
        if StaticFunctions.change_screen_flag:
            self.menu.blit(self.fondo, (0, 0))
            StaticFunctions.change_screen_flag = False

        event_game = pygame.event.get()
        for event in event_game:#Eventos
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Evento generado al presionar el click izquierdo
                if start_button.collidepoint(pygame.mouse.get_pos()):#Llama al evento cuando se presione button_start
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Difficulty")
                    StaticFunctions.change_screen_flag = True
                elif score_button.collidepoint(pygame.mouse.get_pos()):
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("ScoreBoard")
                    StaticFunctions.change_screen_flag = True
                
                elif options_button.collidepoint(pygame.mouse.get_pos()):
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Options")
                    StaticFunctions.change_screen_flag = True
                
                elif music_button.collidepoint(pygame.mouse.get_pos()):
                    self.muteado = not self.muteado
                    if self.muteado:
                        pygame.mixer.music.set_volume(0)#Silencia la música
                    else:
                        pygame.mixer.music.set_volume(0.6)#Vuelve a sonar la musica

                elif exit_button.collidepoint(pygame.mouse.get_pos()):
                    print("Juego cerrado")
                    return False
        return True
#endregion

#region Score
class Scoreboard():
    def __init__(self):
        self.score = StaticFunctions.iniciar_pantalla()
        #Cargar la imagen del fondo
        self.fondo = pygame.image.load("archivos_multimedia/imagenes/fondo_score.png")
        self.fondo = pygame.transform.scale(self.fondo, self.score.get_size())#Escala al tamaño de la pantalla

        self.button_back = [458,715,355, 80]#Posición x, posición Y, Largo, alto
        self.button_music = [1190, 10, 75, 75]

        self.muteado = False

    def init_scoreboard(self):
        back_button = StaticFunctions.dibujar_imagen(self.score, "archivos_multimedia/imagenes/boton_atras_score.png", self.button_back)
        music_button = StaticFunctions.dibujar_imagen(self.score, "archivos_multimedia/imagenes/boton_musica.png", self.button_music)

        if StaticFunctions.change_screen_flag:
            self.score.blit(self.fondo, (0, 0))
            StaticFunctions.iniciar_musica(0.2,-1,"archivos_multimedia/musica/musica_score.mp3")
            StaticFunctions.change_screen_flag = False
        
        event_game = pygame.event.get()
        for event in event_game:
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Evento generado al presionar el click izquierdo
                if music_button.collidepoint(pygame.mouse.get_pos()):
                    self.muteado = not self.muteado
                    if self.muteado:
                        pygame.mixer.music.set_volume(0)#Silencia la música
                    else:
                        pygame.mixer.music.set_volume(0.2)#Vuelve a sonar la musica
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Menu")
                    StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu2.mp3") 
                    StaticFunctions.change_screen_flag = True
        return True
#endregion

#region Options
class Options():
    def __init__(self):
        self.options = StaticFunctions.iniciar_pantalla()
        self.fondo = pygame.image.load("archivos_multimedia/imagenes/imagen_opciones.png")
        self.fondo = pygame.transform.scale(self.fondo, self.options.get_size())#Escala
        self.button_back = [458,715,355, 80]#Posición x,
        self.button_music = [1190, 10, 75, 75]
        self.muteado = False
    
    def init_options(self):
        back_button = StaticFunctions.dibujar_imagen(self.options, "archivos_multimedia/imagenes/boton_atras.png", self.button_back)
        music_button = StaticFunctions.dibujar_imagen(self.options, "archivos_multimedia/imagenes/boton_musica.png", self.button_music)
        
        if StaticFunctions.change_screen_flag:
            self.options.blit(self.fondo, (0, 0))
            StaticFunctions.iniciar_musica(0.2,-1,"archivos_multimedia/musica/musica_menu.mp3")
            StaticFunctions.change_screen_flag = False
            
        event_game = pygame.event.get()
        for event in event_game:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Evento generado al presionar el click izquierdo
                if music_button.collidepoint(pygame.mouse.get_pos()):
                    self.muteado = not self.muteado
                    if self.muteado:
                        pygame.mixer.music.set_volume(0)#Silencia la música
                    else:
                        pygame.mixer.music.set_volume(0.2)#Vuelve a sonar la musica
                if back_button.collidepoint(pygame.mouse.get_pos()):
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Menu")
                    StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu2.mp3") 
                    StaticFunctions.change_screen_flag = True
        return True
#endregion


#region Difficulty

class Difficulty: 
    def __init__(self): 
        self.difficulty = StaticFunctions.iniciar_pantalla()
        self.fondo = pygame.image.load("archivos_multimedia/imagenes/menu_dificultad.png") 
        self.fondo = pygame.transform.scale(self.fondo, self.difficulty.get_size())  # Escala el fondo al tamaño de la pantalla
        
        # Definición de botones como listas [x, y, ancho, alto]
        self.button_easy = [470, 260, 355, 96]
        self.button_medium = [470, 370, 355, 96]
        self.button_hard = [470, 487, 355, 96]
        self.button_back = [458, 715, 355, 80]
        self.button_music = [1190, 10, 75, 75]
        self.muteado = False

    def init_difficulty(self):
        if StaticFunctions.change_screen_flag:
            self.difficulty.blit(self.fondo, (0, 0))
            StaticFunctions.change_screen_flag = False

        button_easy= StaticFunctions.dibujar_imagen(self.difficulty, "archivos_multimedia/imagenes/boton_facil.png", self.button_easy)
        button_medium= StaticFunctions.dibujar_imagen(self.difficulty, "archivos_multimedia/imagenes/boton_medio.png", self.button_medium)
        button_hard= StaticFunctions.dibujar_imagen(self.difficulty, "archivos_multimedia/imagenes/boton_dificil.png", self.button_hard)
        button_back= StaticFunctions.dibujar_imagen(self.difficulty, "archivos_multimedia/imagenes/boton_atras.png", self.button_back)
        button_music= StaticFunctions.dibujar_imagen(self.difficulty, "archivos_multimedia/imagenes/boton_musica.png", self.button_music)
        
        
        event_game = pygame.event.get()
        for event in event_game:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_easy.collidepoint(pygame.mouse.get_pos()):
                    print("Juego Inicializado en Modo FACIL") #Aca se llamaria a la funcion que inicializaria el modo facil
                elif button_medium.collidepoint(pygame.mouse.get_pos()):
                    print("Juego Inicializado en Modo MEDIO") #Aca se llamaria a la funcion que inicializaria el modo medio
                elif button_hard.collidepoint(pygame.mouse.get_pos()):
                    print("Juego Inicializado en Modo DIFICIL") #Aca se llamaria a la funcion que inicializaria el modo dificil
                elif button_back.collidepoint(pygame.mouse.get_pos()):
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Menu") #Vuelve a la pantalla de menu
                    StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu2.mp3") 
                    StaticFunctions.change_screen_flag = True
                elif button_music.collidepoint(pygame.mouse.get_pos()):
                    self.muteado = not self.muteado
                    if self.muteado:
                        pygame.mixer.music.set_volume(0)
                    else:
                        pygame.mixer.music.set_volume(0.2)

        return True
#endregion