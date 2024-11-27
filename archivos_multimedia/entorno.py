import csv  # Necesario para manejar el archivo CSV
import pygame
import csv
import random
import StaticFunctions
from Colors import *

class FinalScreen():
    def __init__(self):
        # Inicializa la pantalla y el fondo
        self.screen = StaticFunctions.iniciar_pantalla()
        self.fondo = pygame.image.load("archivos_multimedia/imagenes/menu_final.png") 
        self.fondo = pygame.transform.scale(self.fondo, self.screen.get_size())

        # Caja de texto
        self.input_box = pygame.Rect(440, 350, 400, 50)
        self.input_active = False
        self.name = ""

        # Botones
        self.submit_button = [540, 480, 150, 60]  # Botón enviar
        self.button_back = [458, 715, 150, 60]  # Botón volver al menú principal

        # Imagen "Tu puntuación"
        self.score_image_path = "archivos_multimedia/imagenes/tu_puntuacion.png"
        self.score_image_size = (200, 60)  # Tamaño 
        self.score_value = 5  # Puntaje estático inicial, se reemplazará con `score_mod_tomas`

        # Fuente y colores
        self.font = pygame.font.SysFont("Arial", 30, True, False)
        self.color_active = pygame.Color('dodgerblue2')
        self.color_inactive = pygame.Color('lightskyblue3')

    def guardar_puntaje(self, nombre, puntaje):
        """
        Guarda el nombre y puntaje en el archivo scoreboard.csv.
        Crea el archivo si no existe.
        """
        filepath = "archivos_multimedia/scoreboard.csv"
        with open(filepath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, puntaje])

    def init_final_screen(self, score_mod_tomas):  # Cambiado para aceptar puntaje dinámico
        """
        Inicializa la pantalla final.
        Recibe el puntaje desde el menú anterior mediante la variable `score_mod_tomas`.
        """
        self.score_value = score_mod_tomas  # Actualiza el puntaje dinámicamente

        # Dibuja el fondo
        self.screen.blit(self.fondo, (0, 0))
        
        score_image_path = "archivos_multimedia/imagenes/tu_puntuacion.png"
        score_image_size = (400, 100)  
        StaticFunctions.dibujar_imagen(self.screen, score_image_path, [360, 250, *score_image_size])

        # Dibuja el puntaje al lado de la imagen
        score_text_position = [700, 265]  # Coordenadas ajustadas
        StaticFunctions.dibujar_texto(
            self.screen,
            f"{self.score_value} puntos",
            40,  # Tamaño de fuente más grande para claridad
            pygame.Color('white'),
            score_text_position,
            is_bold=True,
            is_italic=False
        )

        # Dibuja la caja de texto
        box_color = self.color_active if self.input_active else self.color_inactive
        pygame.draw.rect(self.screen, pygame.Color("#6b2d6a"), self.input_box)
        pygame.draw.rect(self.screen, box_color, self.input_box, 2)
        name_text = self.font.render(self.name, True, pygame.Color('white'))
        self.screen.blit(name_text, (self.input_box.x + 5, self.input_box.y + 10))

        # Botones: Reducir tamaño y ajustar posición
        submit_button_path = "archivos_multimedia/imagenes/boton_guardar.png"
        back_button_path = "archivos_multimedia/imagenes/boton_volver.png"

        submit_button_size = [509.1, 440, 261.8, 64]
        back_button_size = [539.6, 700, 200.8, 64]

        StaticFunctions.dibujar_imagen(self.screen, submit_button_path, submit_button_size)
        StaticFunctions.dibujar_imagen(self.screen, back_button_path, back_button_size)

        # Manejo de eventos
        event_game = pygame.event.get()
        for event in event_game:
            if event.type == pygame.QUIT:
                return False

            # Click en la caja de texto o botones
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.input_box.collidepoint(event.pos):
                    self.input_active = True
                else:
                    self.input_active = False

                if pygame.Rect(*submit_button_size).collidepoint(event.pos):
                    if self.name:
                        print("Nombre ingresado:", self.name)
                        print("Puntuación enviada:", self.score_value)
                        self.guardar_puntaje(self.name, self.score_value)  # Guardar en CSV

                if pygame.Rect(*back_button_size).collidepoint(event.pos):
                    print("Volviendo al menú principal...")
                    StaticFunctions.change_screen_flag = True

            # Manejo de teclado
            if event.type == pygame.KEYDOWN and self.input_active:
                if event.key == pygame.K_RETURN:
                    if self.name:
                        print("Nombre ingresado (Enter):", self.name)
                        print("Puntuación enviada:", self.score_value)
                        self.guardar_puntaje(self.name, self.score_value)  # Guardar en CSV
                elif event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]
                else:
                    if event.unicode.isalpha():
                        self.name += event.unicode

        return True
