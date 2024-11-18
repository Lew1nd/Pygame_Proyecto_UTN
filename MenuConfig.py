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
        StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu.mp3")
        pygame.display.set_icon(icono)
        self.screen_color = BLUEVIOLET

        #botones
        self.button_start = [500, 250,250,100]#Posición x, posición Y, Largo, alto
        self.button_score = [500, 450,250,100]
        self.button_exit = [500,650,250,100]
        self.button_music = [1180, 20, 100, 70]

        #textos
        self.text_tittle = [470,100]

        #imagen muestra (temporal)
        self.imagen_1 = [0,0,500,500]

        self.muteado = False

    def init_menu(self):
        tittle_text = StaticFunctions.dibujar_texto(self.menu, "Preguntados", 70, GREEN, self.text_tittle)
        start_button = StaticFunctions.generar_rectangulo(self.menu, GREEN, self.button_start)
        score_button = StaticFunctions.generar_rectangulo(self.menu, YELLOW1, self.button_score)
        music_button = StaticFunctions.generar_rectangulo(self.menu, BLUE, self.button_music)
        exit_button = StaticFunctions.generar_rectangulo(self.menu, RED1, self.button_exit)

        #img1 = StaticFunctions.dibujar_imagen(self.menu, "archivos_multimedia/imagenes/icono_preguntados.png", self.imagen_1)#imagen de preguntados
        
        if StaticFunctions.change_screen_flag:
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
        self.screen_color = GREEN1

        self.button_back = [500,650,250,100]
        self.button_music = [1180, 20, 100, 70]

        self.muteado = False

    def init_scoreboard(self):
        back_button = StaticFunctions.generar_rectangulo(self.score, RED1, self.button_back)
        music_button = StaticFunctions.generar_rectangulo(self.score, BLUE, self.button_music)

        if StaticFunctions.change_screen_flag:
            self.score.fill(self.screen_color)
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
                    StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu.mp3") 
                    StaticFunctions.change_screen_flag = True
        return True
#endregion