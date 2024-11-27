'''
Aquí estará todo lo relacionado a las pantallas
'''
import pygame
import csv
import random
import StaticFunctions
from Colors import *
#region Menú
class Menu():
    def __init__(self):
        self.menu = StaticFunctions.iniciar_pantalla()
        pygame.display.set_caption ("BGB")
        icono = pygame.image.load("archivos_multimedia/imagenes/icono_preguntados.png")#Carga el incono de la ventana
        #musica
        self.sonido_advertencia = pygame.mixer.Sound("archivos_multimedia/musica/sonido_timer.mp3")
        self.sonido_advertencia.set_volume(0.5)
        StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu2.mp3")
        pygame.display.set_icon(icono)
        self.muteado = False
        
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

    def init_menu(self):
        '''
        Inicializador de la pantalla, se ejecuta constantemente en Core
        '''
        self.menu.blit(self.fondo, (0, 0))
        start_button = StaticFunctions.dibujar_imagen(self.menu,"archivos_multimedia/imagenes/boton_jugar.png" , self.button_start)
        score_button = StaticFunctions.dibujar_imagen(self.menu, "archivos_multimedia/imagenes/boton_score.png", self.button_score)
        music_button = StaticFunctions.dibujar_imagen(self.menu,"archivos_multimedia/imagenes/boton_musica.png", self.button_music)
        options_button = StaticFunctions.dibujar_imagen(self.menu, "archivos_multimedia/imagenes/boton_ajustes.png", self.button_options)
        exit_button = StaticFunctions.dibujar_imagen(self.menu, "archivos_multimedia/imagenes/boton_salir.png", self.button_exit)
        
        if StaticFunctions.change_screen_flag:
            self.menu.blit(self.fondo, (0, 0))
            StaticFunctions.change_screen_flag = False

        event_game = pygame.event.get()
        for event in event_game:#Eventos
            if event.type == pygame.QUIT:
                return False
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#Evento generado al presionar el click izquierdo
                if start_button.collidepoint(pygame.mouse.get_pos()):#Llama al evento cuando se presione button_start
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Categories")
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
        '''
        Inicializador de la pantalla, se ejecuta constantemente en Core
        '''
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
        self.button_question = [900, 700, 355, 80]
        self.button_confirm_changes = [900,600,355,80]

        self.text_lives, self.text_lives_input = [50,500], [250, 520] 
        self.text_score, self.text_score_input = [50, 300], [680, 320]
        self.text_time, self.text_time_input = [40, 700], [300,720]
        
        #self.lives = str(StaticFunctions.lives)
        #self.score = str(StaticFunctions.score_gain_per_question)
        #self.time = str(StaticFunctions.time)
        
        self.text_selected = [0,0]

        self.muteado = False
        self.text_focus = [False,False,False]

    def seleccionar_texto(self, selected_text: int):
        '''
        Permite establecer foco en una cadena de texto para permitir la escritura. Desactiva el foco de las demás cadenas existentes.\n
        Recibe un índice para una lista que posteriormente se utilizará para activar la casilla de texto correspondiente
        No devuelve nada
        '''
        self.text_focus[:] = [False] * len(self.text_focus)
        self.text_focus[selected_text] = True
    
    def modificar_texto(self, event, value_selected: str, selected_text: int, max_value: int):
        '''
        Permite modificar el texto a partir de la entrada del usuarios
        Recibe el gestionador de eventos, el valor que se modificará, la entrada de texto que se modificará y el valor máximo permitido
        No devuelve nada
        '''
        if self.text_focus[selected_text]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    value_selected = StaticFunctions.suprimir_texto(self.options, self.fondo, event, value_selected)
                else:
                    value_selected = StaticFunctions.entrada_texto(self.options, self.fondo, event, value_selected, max_value, True)

                match selected_text:
                    case 0: StaticFunctions.lives = value_selected
                    case 1: StaticFunctions.score_gain_per_question = value_selected
                    case 2: StaticFunctions.time_config = value_selected

    def init_options(self):
        '''
        Inicializador de la pantalla, se ejecuta constantemente en Core
        '''
        back_button = StaticFunctions.dibujar_imagen(self.options, "archivos_multimedia/imagenes/boton_atras.png", self.button_back)
        music_button = StaticFunctions.dibujar_imagen(self.options, "archivos_multimedia/imagenes/boton_musica.png", self.button_music)
        questions_button = StaticFunctions.generar_rectangulo(self.options, GREEN, self.button_question)
        confirm_changes_button = StaticFunctions.generar_rectangulo(self.options, BLUE, self.button_confirm_changes)
        
        lives_text = StaticFunctions.dibujar_texto(self.options, "Vidas: ", 70, YELLOW1, self.text_lives, True, False)
        lives_input_text = StaticFunctions.dibujar_texto(self.options, str(StaticFunctions.lives), 50, RED1, self.text_lives_input, True, False)

        score_text = StaticFunctions.dibujar_texto(self.options, "Puntaje por pregunta: ", 70, YELLOW1, self.text_score, True, False)
        score_input_text = StaticFunctions.dibujar_texto(self.options, str(StaticFunctions.score_gain_per_question), 50, RED1, self.text_score_input, True, False)

        time_text = StaticFunctions.dibujar_texto(self.options, "Tiempo: ", 70, YELLOW1, self.text_time, True, False)
        time_input_text = StaticFunctions.dibujar_texto(self.options, str(StaticFunctions.time_config), 50, RED1, self.text_time_input, True, False)

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
                elif back_button.collidepoint(pygame.mouse.get_pos()) and not any(self.text_focus) == True:
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Menu")
                    StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu2.mp3") 
                    StaticFunctions.change_screen_flag = True
                elif questions_button.collidepoint(pygame.mouse.get_pos()) and not any(self.text_focus) == True:
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("QuestionManager")
                    StaticFunctions.change_screen_flag = True
                elif confirm_changes_button.collidepoint(pygame.mouse.get_pos()) and not any(self.text_focus) == True:
                    StaticFunctions.guardar_datos(StaticFunctions.player_datapath, "Player", 'w')
                    StaticFunctions.cargar_datos(StaticFunctions.player_datapath, "Player")
                elif lives_input_text.collidepoint(pygame.mouse.get_pos()): StaticFunctions.seleccionar_texto(self.text_focus, 0) 
                elif score_input_text.collidepoint(pygame.mouse.get_pos()): StaticFunctions.seleccionar_texto(self.text_focus,1)
                elif time_input_text.collidepoint(pygame.mouse.get_pos()): StaticFunctions.seleccionar_texto(self.text_focus,2)  
                else:
                    StaticFunctions.texto_vacio(self.text_focus, str(StaticFunctions.lives), 0)
                    StaticFunctions.texto_vacio(self.text_focus, str(StaticFunctions.score_gain_per_question), 1)
                    StaticFunctions.texto_vacio(self.text_focus, str(StaticFunctions.time_config), 2)
                
            self.modificar_texto(event,str(StaticFunctions.lives),0, 99)
            self.modificar_texto(event,str(StaticFunctions.score_gain_per_question),1, 100000)
            self.modificar_texto(event,str(StaticFunctions.time_config),2, 1800)#El parámetro 3 es el tiempo máximo permitido. Ponerlo en segundos
        return True
#endregion
#region Agregar preguntas
class QuestionManager():
    def __init__(self):
        self.question_manager = StaticFunctions.iniciar_pantalla()

        self.fondo = pygame.image.load("archivos_multimedia/imagenes/imagen_opciones.png")
        self.fondo = pygame.transform.scale(self.fondo, self.question_manager.get_size())#Escala
        
        self.button_back = [458,715,355, 80]#Posición x,
        self.button_music = [1190, 10, 75, 75]
        self.button_confirm_changes = [850, 700, 100, 100]

        self.question = [50,50,550,50]
        self.answer1, self.answer2, self.answer3, self.answer4 = [50, 200, 550, 50], [50, 300, 550, 50], [50, 400, 550, 50], [50, 500, 550, 50]

        self.text_question = [50, 50]
        self.text_answer1, self.text_answer2, self.text_answer3, self.text_answer4  = [50, 200], [50, 300], [50, 400], [50, 500]

        self.categories = ["Anime", "Videojuegos", "Geografía"]
        self.categories_texts = [[650,200],
                                 [650, 300],
                                 [650, 350],
                                 [650, 400]]

        self.difficulty = ["Fácil", "Medio", "Difícil"]
        self.difficulty_texts = [[900, 200],
                                 [900, 300],
                                 [900, 350],
                                 [900, 400]]

        self.muteado = False
        self.layer_selected = False
        self.text_focus = [False,False,False,False,False]

        self.questions = ["","","","","",""]

    def modificar_texto(self, event, selected_text: int, max_value: int):
        '''
        Permite modificar el texto a partir de la entrada del usuario.\n
        Recibe el gestionador de enventos, el indice del texto seleccionado y un valor máximo de números enteros.\n
        No devuelve nada.
        '''
        if self.text_focus[selected_text]:
            selected_value = StaticFunctions.questions[selected_text]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    selected_value = selected_value[:-1] 
                else:
                    selected_value = StaticFunctions.entrada_texto(
                        self.question_manager, self.fondo, event, selected_value, max_value, False)
            StaticFunctions.questions[selected_text] = selected_value

    def seleccionar_tipo_pregunta(self, value: str, is_category: bool):
        '''
        Carga la opción elegida según la elección del jugador.\n
        Recibe el valor (puede ser categoría o dificultad) y un booleano que comprueba si es una categoría o una dificultad.\n
        No devuelve nada.
        '''
        if is_category: StaticFunctions.selected_category = str(value)
        else: StaticFunctions.selected_difficulty = str(value)
            
    def init_question_manager(self):
        '''
        Inicializador de la pantalla, se ejecuta constantemente en Core
        '''
        back_button = StaticFunctions.dibujar_imagen(self.question_manager, "archivos_multimedia/imagenes/boton_atras.png", self.button_back)
        music_button = StaticFunctions.dibujar_imagen(self.question_manager, "archivos_multimedia/imagenes/boton_musica.png", self.button_music)
        confirm_changes_button = StaticFunctions.generar_rectangulo(self.question_manager, BLUE, self.button_confirm_changes)

        question_layer = StaticFunctions.generar_rectangulo(self.question_manager, GREEN, self.question)
        answer1_layer = StaticFunctions.generar_rectangulo(self.question_manager, GREEN, self.answer1)
        answer2_layer = StaticFunctions.generar_rectangulo(self.question_manager, GREEN, self.answer2)
        answer3_layer = StaticFunctions.generar_rectangulo(self.question_manager, GREEN, self.answer3)
        answer4_layer = StaticFunctions.generar_rectangulo(self.question_manager, GREEN, self.answer4)

        question_text = StaticFunctions.dibujar_texto(self.question_manager, StaticFunctions.questions[0], 40, RED1, self.text_question, False, False)
        answer1_text = StaticFunctions.dibujar_texto(self.question_manager, StaticFunctions.questions[1], 40, RED1, self.text_answer1, False, False)
        answer2_text = StaticFunctions.dibujar_texto(self.question_manager, StaticFunctions.questions[2], 40, RED1, self.text_answer2, False, False)
        answer3_text = StaticFunctions.dibujar_texto(self.question_manager, StaticFunctions.questions[3], 40, RED1, self.text_answer3, False, False)
        answer4_text = StaticFunctions.dibujar_texto(self.question_manager, StaticFunctions.questions[4], 40, RED1, self.text_answer4, False, False)

        category_name_text = StaticFunctions.dibujar_texto(self.question_manager, "Categoría", 40, RED1, self.categories_texts[0], True, False)
        category1_text = StaticFunctions.dibujar_texto(self.question_manager, self.categories[0], 40, RED1, self.categories_texts[1], False, False)
        category2_text = StaticFunctions.dibujar_texto(self.question_manager, self.categories[1], 40, RED1, self.categories_texts[2], False, False)
        category3_text = StaticFunctions.dibujar_texto(self.question_manager, self.categories[2], 40, RED1, self.categories_texts[3], False, False)

        difficulty_name_text = StaticFunctions.dibujar_texto(self.question_manager, "Dificultad", 40, RED1, self.difficulty_texts[0], True, False)
        difficulty1_text = StaticFunctions.dibujar_texto(self.question_manager, self.difficulty[0], 40, RED1, self.difficulty_texts[1], False, False)
        difficulty2_text = StaticFunctions.dibujar_texto(self.question_manager, self.difficulty[1], 40, RED1, self.difficulty_texts[2], False, False)
        difficulty3_text = StaticFunctions.dibujar_texto(self.question_manager, self.difficulty[2], 40, RED1, self.difficulty_texts[3], False, False)

        selectable_layers = [(question_layer, 0), 
                           (answer1_layer, 1),
                           (answer2_layer, 2),
                           (answer3_layer, 3),
                           (answer4_layer, 4)]
        
        selectable_options = [(category1_text, 0),
                              (category2_text, 1),
                              (category3_text, 2),
                              (difficulty1_text, 3),
                              (difficulty2_text, 4),
                              (difficulty3_text, 5)]

        if StaticFunctions.change_screen_flag:
            self.question_manager.blit(self.fondo, (0, 0))
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
                elif back_button.collidepoint(pygame.mouse.get_pos()) and not any(self.text_focus) == True:
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Options")
                    StaticFunctions.iniciar_musica(0.6,-1,"archivos_multimedia/musica/musica_menu2.mp3") 
                    StaticFunctions.change_screen_flag = True
                elif confirm_changes_button.collidepoint(pygame.mouse.get_pos()) and not any(self.text_focus) == True:
                    StaticFunctions.guardar_datos(StaticFunctions.questions_datapath, "Question_add", 'a')
                    print("Cambios efectuados")
                else:
                    self.layer_selected = False
                    for layer, index in selectable_layers:
                        if layer.collidepoint(pygame.mouse.get_pos()):
                            StaticFunctions.seleccionar_texto(self.text_focus, index)
                            StaticFunctions.questions[index] = ""
                            self.layer_selected = True
                            break
                        if not self.layer_selected:
                            for i in range(len(self.text_focus)): StaticFunctions.texto_vacio(self.text_focus, StaticFunctions.questions[i-1], i)
                    
                    for option, index in selectable_options:
                        if option.collidepoint(pygame.mouse.get_pos()):
                            if index < 3:  self.seleccionar_tipo_pregunta(self.categories[index], False)
                            else: self.seleccionar_tipo_pregunta(self.difficulty[index-3], True)

            for i in range(len(self.text_focus)): self.modificar_texto(event, i-1, i)
        return True

#endregion

#region Difficulty

class Difficulty(): 
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
        '''
        Inicializador de la pantalla, se ejecuta constantemente en Core
        '''
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
                    StaticFunctions.difficulty_game = "Fácil"
                    StaticFunctions.change_screen_flag = True
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Game")
                elif button_medium.collidepoint(pygame.mouse.get_pos()):
                    print("Juego Inicializado en Modo MEDIO") #Aca se llamaria a la funcion que inicializaria el modo medio
                    StaticFunctions.difficulty_game = "Normal"
                    StaticFunctions.change_screen_flag = True
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Game")
                elif button_hard.collidepoint(pygame.mouse.get_pos()):
                    print("Juego Inicializado en Modo DIFICIL") #Aca se llamaria a la funcion que inicializaria el modo dificil
                    StaticFunctions.difficulty_game = "Difícil"
                    StaticFunctions.change_screen_flag = True
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Game")
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

#region Categories  
class Categories():
    def __init__(self):
        self.categories = StaticFunctions.iniciar_pantalla()
        self.fondo = pygame.image.load("archivos_multimedia/imagenes/menu_categorias.png") 
        self.fondo = pygame.transform.scale(self.fondo, self.categories.get_size()) 
        
        self.button_back = [458, 715, 355, 80]
        self.button_music = [1190, 10, 75, 75]
        self.button_anime = [0, 0, 444,800]
        self.button_games = [444, 0, 444, 800]
        self.button_geography = [888,0, 444, 800]
        self.muteado = False

    def init_categories(self):
        if StaticFunctions.change_screen_flag:
            self.categories.blit(self.fondo, (0, 0))
            StaticFunctions.change_screen_flag = False 
            
        button_back= StaticFunctions.dibujar_imagen(self.categories, "archivos_multimedia/imagenes/boton_atras.png", self.button_back)
        button_music= StaticFunctions.dibujar_imagen(self.categories, "archivos_multimedia/imagenes/boton_musica.png", self.button_music)

        event_game = pygame.event.get()
        for event in event_game:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                
                if button_back.collidepoint(pygame.mouse.get_pos()):
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Menu") 
                    StaticFunctions.iniciar_musica(0.6, -1, "archivos_multimedia/musica/musica_menu2.mp3") 
                    StaticFunctions.change_screen_flag = True
                
                elif button_music.collidepoint(pygame.mouse.get_pos()):
                    self.muteado = not self.muteado
                    if self.muteado:
                        pygame.mixer.music.set_volume(0)  
                    else:
                        pygame.mixer.music.set_volume(0.2)   
                
                elif self.button_anime[0] <= pygame.mouse.get_pos()[0] <= self.button_anime[0] + self.button_anime[2] and \
                    self.button_anime[1] <= pygame.mouse.get_pos()[1] <= self.button_anime[1] + self.button_anime[3]: # Separ elif por lineas para que sea mas legible
                    StaticFunctions.category_game = "Anime"
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Difficulty")
                    StaticFunctions.change_screen_flag = True
                    print("Categoria seleccionada: ANIME")   
                elif self.button_games[0] <= pygame.mouse.get_pos()[0] <= self.button_games[0] + self.button_games[2] and \
                    self.button_games[1] <= pygame.mouse.get_pos()[1] <= self.button_games[1] + self.button_games[3]:# Separe elif por lineas para que sea mas legibleç
                    StaticFunctions.category_game = "Videojuegos"
                    StaticFunctions.change_screen_flag = True
                    print("Categoria seleccionada: VIDEOJUEGOS")
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Difficulty")
                elif self.button_geography[0] <= pygame.mouse.get_pos()[0] <= self.button_geography[0] + self.button_geography[2] and \
                    self.button_geography[1] <= pygame.mouse.get_pos()[1] <= self.button_geography[1] + self.button_geography[3]:# Separe elif por lineas para que sea mas legible
                    print("Categoria seleccionada: GEOGRAFIA")
                    StaticFunctions.category_game = "Geografía"
                    StaticFunctions.change_screen_flag = True
                    StaticFunctions.current_screen = StaticFunctions.cambiar_pantalla("Difficulty")   
        return True

#endregion
#region Game

class Game():
    def __init__(self):
        self.game = StaticFunctions.iniciar_pantalla()
        self.fondo = pygame.image.load("archivos_multimedia/imagenes/imagen_opciones.png") 
        self.fondo = pygame.transform.scale(self.fondo, self.game.get_size()) 

        self.buttons = {'Question_layer': [350,100,650, 100],
                        'Option1': [350,300,650,50],
                        'Option2': [350,400,650,50],
                        'Option3': [350,500,650,50],
                        'Option4': [350,600,650,50],
                        'Next_Option': [600,700,150,150],
                        'Music': [1190, 10, 75, 75]}
        
        self.texts = {'Option1': [350,300],
                      'Option2': [350,400],
                      'Option3': [350,500],
                      'Option4': [350,600],
                      'Time_layer': [10,10],
                      'Lives_layer': [10,80],
                      'Lives_value': [142,81],
                      'Timer': [140, 22],
                      'Result_answer': [350,200]}

        self.question_selected = {}#Se guardarán todas las preguntas posible según la categoría y dificultad elegida
        self.question_generated = []#Las preguntas que ya aparecieron se van a guardar aquí, para evitar la repetición
        self.question_saved = {}

        self.can_select_next_question = False
        self.answer_selected = False
        self.game_finished = False
        self.is_correct = False
        self.time_out = True
        self.muteado = False

        self.current_lives = 0
        self.game_time = 0 #Tiempo transcurrido en la partida
        self.score_points = 0

        self.segundos_restantes = StaticFunctions.timer
        self.evento_timer = pygame.USEREVENT
        pygame.time.set_timer(self.evento_timer, 1000)

    def obtener_pregunta_aleatoria(self):
        '''
        Obtiene una pregunta de manera aleatoria entre todas las que se obtuvo según la categoría y dificultad.\n
        No recibe ni devuelve nada.
        '''
        self.game_finished = self.derrota()
        while self.game_finished == False:
            self.question_selected = random.choice(StaticFunctions.all_questions_data)
            if not self.pregunta_repetida(self.question_selected): 
                self.question_saved[self.question_selected['Pregunta']] = self.question_selected #Guarda la pregunta utilizando la pregunta como clave
                break
            
        self.question_generated.append(self.question_selected['Pregunta'])
        self.answer_selected, self.can_select_next_question = False, False
    
    def pregunta_repetida(self, question_dict: dict):
        '''
        Comprueba si la pregunta que se eligió no es repetida, en caso de serlo, retorna True y vuelve a generar otra.\n
        Recibe un diccionario con las preguntas que ya aparecieron.\n
        Devuelve True o Flase según el caso.
        '''
        if not len(self.question_generated) >= len(StaticFunctions.all_questions_data):
            for question in self.question_generated:
                if question_dict['Pregunta'] == question:
                    return True
        else: self.game_finished = True
        return False

    def mostrar_respuesta(self, is_correct: bool):
        '''
        Muestra un texto con un color dependiendo de si el jugador repondió la respuesta correctamente.\n
        Recibe un booleano que comprueba el resultado.\n
        Devuelve una tupla con un string de "Respuesta correcta o incorrecta", además del color que utilizará el texto.
        '''
        if (is_correct): return "Respuesta correcta", GREEN
        elif (self.time_out == True): 
            StaticFunctions.timer = StaticFunctions.time_config
            return "Tiempo excedido", RED1
        elif(self.time_out == False): return "Respuesta incorrecta", RED1
            
    def calcular_respuesta(self, option_selected: int):
        '''
        Función encargada de determinar si la respuesta del usuario es correcta o no.\n
        Recibe la opción seleccionada como un entero, que luego se comprobará con el número de registro en el archivo,
        si es igual, entonces la respuesta es correcta.\n
        No devuelve nada.
        '''
        self.question_selected['Veces preguntada'] = int(self.question_selected['Veces preguntada']) + 1
        self.answer_selected, self.can_select_next_question = True, True

        correct_answer = self.question_selected['Correcta']
        correct_answer = int(correct_answer)

        if option_selected == correct_answer:#Si la opción es correcta, se le suma 5 segundos
            self.is_correct = True
            self.question_selected['Cantidad aciertos'] = int(self.question_selected['Cantidad aciertos']) + 1
            self.score_points += StaticFunctions.score_gain_per_question
            StaticFunctions.timer += 5
        else:#Caso opuesto, pierde una vida
            self.is_correct = False
            self.question_selected['Cantidad fallos'] = int(self.question_selected['Cantidad fallos']) + 1
            self.current_lives -= 1

    def eliminar_registros_con_None(self, content):
        '''
        Elimina registros que tengan valores inválidos, como None\n.
        Recibe el content, que será el contenido que fue leido mediante un CSV.reader.\n
        Devuelve el mismo content mediante bucle eliminando cualquier registro inválido.
        '''
        return [pregunta for pregunta in content if None not in pregunta and all(v != '' for v in pregunta.values())]
        #La pregunta, por la key de la pregunta en el contenido, si es nulo, lo descarta, si algún registro de la key es '', lo descarta

    def actualizar_registros(self, datapath):
        questions = []

        with open(datapath, 'r', newline='', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            questions = list(reader)

        questions = self.eliminar_registros_con_None(questions)#Debido a que se lee un registro de más, se lo filtra
    
        for question in questions:
            Key_question = question['Pregunta']
            if Key_question in self.question_saved:#Si las preguntas que aparecieron en la partida aparecen en el archivo, se actualizan sus valores
                question['Cantidad fallos'] = self.question_saved[Key_question]['Cantidad fallos']
                question['Cantidad aciertos'] = self.question_saved[Key_question]['Cantidad aciertos']
                question['Veces preguntada'] = self.question_saved[Key_question]['Veces preguntada']
        #--------------------------------------------Escritura----------------------------------
        with open(datapath, 'w', newline='', encoding='utf-8') as archivo:
            fieldnames = ['Pregunta', 'Opción A', 'Opción B', 'Opción C', 'Opción D', 
                          'Correcta', 'Categoría', 'Dificultad', 'Cantidad fallos', 
                          'Cantidad aciertos', 'Veces preguntada']
            writer = csv.DictWriter(archivo, fieldnames=fieldnames)
            writer.writeheader()

            for question in questions: writer.writerow(question)    

    def derrota(self):
        '''
        Encargado de determinar el fin del juego en base a las vidas, si el jugador pierde todas sus vidas, el juego se acaba.\n
        No recibe nada.\n
        Devuelve True en caso de perder todas las vidas, False en caso contrario.
        '''
        if self.current_lives < 1: return True
        else: return False

    #-------------------------------------------------------------------------------------------
    def init_game(self):
        '''
        Inicializador de la pantalla, se ejecuta constantemente en Core
        '''
        self.game.blit(self.fondo, (0, 0))
        if StaticFunctions.change_screen_flag:
            self.current_lives = StaticFunctions.lives
            StaticFunctions.cargar_datos(StaticFunctions.questions_datapath,"Start")
            StaticFunctions.change_screen_flag = False 
            self.obtener_pregunta_aleatoria()
        # if self.segundos_restantes <= 13: #cambia el color y reproduce el sonido de que el tiempo se agota
        #     color = (255, 0, 0) 
        #     if not self.sonido_advertencia_reproducido:
        #         self.sonido_advertencia.play()
        #         self.sonido_advertencia_reproducido = True
        # else:
        #     color = COLOR_AMARILLO
        #     self.sonido_advertencia_reproducido = False
        # if self.segundos_restantes <= 5 and self.segundos_restantes % 2 == 0:
        #     color = (255, 255, 255) 

        timer = StaticFunctions.mostrar_timer(self.game, YELLOW1, StaticFunctions.timer, self.texts['Timer'])#Funcion que muestra el temporizador.
        pygame.draw.rect(self.game, (255,255,255), (135, 16, 50, 40), border_radius=10, width=4)# Dibujar un marco alrededor del temporizador.
        pygame.draw.rect(self.game, (255,255,255), (135, 85, 50, 40), border_radius=10, width=4)# Dibujar un marco alrededor de las vidas.
        music_button = StaticFunctions.dibujar_imagen(self.game, "archivos_multimedia/imagenes/boton_musica.png", self.buttons['Music'])

        if(self.game_finished == False):
            question_layer = StaticFunctions.generar_rectangulo_estilizado(self.game, WHITE, self.buttons['Question_layer'], (0, 0, 0), 3, redondeo=10)
            button_option1 = StaticFunctions.generar_rectangulo_estilizado(self.game, WHITE, self.buttons['Option1'], (0, 0, 0), 3, redondeo=10)
            button_option2 = StaticFunctions.generar_rectangulo_estilizado(self.game, WHITE, self.buttons['Option2'], (0, 0, 0), 3, redondeo=10)
            button_option3 = StaticFunctions.generar_rectangulo_estilizado(self.game, WHITE, self.buttons['Option3'], (0, 0, 0), 3, redondeo=10)
            button_option4 = StaticFunctions.generar_rectangulo_estilizado(self.game, WHITE, self.buttons['Option4'], (0, 0, 0), 3, redondeo=10)

            text_question = StaticFunctions.dibujar_texto_estilizado(
                self.game, 
                self.question_selected['Pregunta'], 
                tamano=24, 
                color=BLACK, 
                posicion=self.buttons['Question_layer'], 
                centrado_horizontal=True, 
                centrado_vertical=True, 
                fuente="Comic Sans MS", 
                negrita=True
            )

            text_answer1 = StaticFunctions.dibujar_texto_estilizado(
                self.game, 
                self.question_selected['Opción A'], 
                tamano=30, 
                color=BLACK, 
                posicion=self.buttons['Option1'], 
                centrado_horizontal=True, 
                centrado_vertical=True, 
                negrita=True,
                fuente_archivo="archivos_multimedia/fuentes/LeagueSpartan-Regular.ttf"
            )

            text_answer2 = StaticFunctions.dibujar_texto_estilizado(
                self.game, 
                self.question_selected['Opción B'], 
                30, 
                BLACK, 
                self.buttons['Option2'], 
                centrado_horizontal=True, 
                centrado_vertical=True, 
                fuente_archivo="archivos_multimedia/fuentes/LeagueSpartan-Regular.ttf"
            )

            text_answer3 = StaticFunctions.dibujar_texto_estilizado(
                self.game, 
                self.question_selected['Opción C'], 
                30, 
                BLACK, 
                self.buttons['Option3'], 
                centrado_horizontal=True, 
                centrado_vertical=True, 
                fuente_archivo="archivos_multimedia/fuentes/LeagueSpartan-Regular.ttf"
            )

            text_answer4 = StaticFunctions.dibujar_texto_estilizado(
                self.game, 
                self.question_selected['Opción D'], 
                30, 
                BLACK, 
                self.buttons['Option4'], 
                centrado_horizontal=True, 
                centrado_vertical=True, 
                fuente_archivo="archivos_multimedia/fuentes/LeagueSpartan-Regular.ttf"
            )

        else:
            StaticFunctions.dibujar_imagen(self.game,"archivos_multimedia/imagenes/game_over.png",[0,0,self.game.get_size()[0],self.game.get_size()[1]]) 
            
        if(self.can_select_next_question == True):
            text_result = StaticFunctions.dibujar_texto(self.game, self.mostrar_respuesta(self.is_correct)[0], 30, self.mostrar_respuesta(self.is_correct)[1], self.texts['Result_answer'],False,False)

        text_timer = StaticFunctions.dibujar_texto(self.game, "Tiempo", 40, YELLOW1, self.texts['Time_layer'], True, False)
        text_lives_layer = StaticFunctions.dibujar_texto(self.game, "Vidas", 40, YELLOW1, self.texts['Lives_layer'], True, False)
        text_lives = StaticFunctions.dibujar_texto(self.game, str(self.current_lives), 40, GREEN, self.texts['Lives_value'], True, False)

        # Ajustamos dimensiones y posición del botón "Siguiente"
        self.buttons['Next_Option'] = [540, 700, 261, 64]  # (x, y, ancho, alto)

        # Dibujamos la imagen del botón con las dimensiones ajustadas
        button_next_option = StaticFunctions.dibujar_imagen(
            self.game,
            "archivos_multimedia/imagenes/boton_siguiente.png",
            self.buttons['Next_Option']
        )


        event_game = pygame.event.get()
        for event in event_game:
            if event.type == pygame.QUIT:
                return False
            
            #evento de temporizador
            if self.answer_selected == False and self.game_finished == False:
                if event.type == self.evento_timer:
                    if StaticFunctions.timer > 0:
                        self.game_time += 1
                        StaticFunctions.timer -= 1
                        self.time_out = False
                    else:
                        self.is_correct = False
                        self.current_lives -= 1
                        self.can_select_next_question, self.answer_selected, self.time_out = True, True, True


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if music_button.collidepoint(pygame.mouse.get_pos()):
                    self.muteado = not self.muteado
                    if self.muteado: pygame.mixer.music.set_volume(0)#Silencia la música
                    else: pygame.mixer.music.set_volume(0.6)#Vuelve a sonar la musica
                        
                if(self.game_finished == False):
                    if button_option1.collidepoint(pygame.mouse.get_pos()) and self.answer_selected == False: self.calcular_respuesta(1)
                    elif button_option2.collidepoint(pygame.mouse.get_pos()) and self.answer_selected == False: self.calcular_respuesta(2)
                    elif button_option3.collidepoint(pygame.mouse.get_pos()) and self.answer_selected == False: self.calcular_respuesta(3)
                    elif button_option4.collidepoint(pygame.mouse.get_pos()) and self.answer_selected == False: self.calcular_respuesta(4) 
                    elif button_next_option.collidepoint(pygame.mouse.get_pos()) and self.can_select_next_question == True: self.obtener_pregunta_aleatoria()
                elif button_next_option.collidepoint(pygame.mouse.get_pos()) and self.game_finished == True:
                    self.actualizar_registros(StaticFunctions.questions_datapath)
                    self.is_correct = False
                    print("Yendo a resultados...")
                    StaticFunctions.current_screen = "FinalScreen"
                    
                    
        return True
    
#endregion

#region final screen

class FinalScreen:
    def __init__(self):
        # Inicializa la pantalla y el fondo
        self.screen = StaticFunctions.iniciar_pantalla()
        self.fondo = pygame.image.load("archivos_multimedia/imagenes/menu_final.png") 
        self.fondo = pygame.transform.scale(self.fondo, self.screen.get_size())

        # Caja de texto
        self.input_box = pygame.Rect(380, 350, 480, 50)
        self.input_active = False
        self.name = ""

        # Botones
        self.submit_button = [508, 480, 200, 60]  # Ajustamos el botón guardar
        self.button_back = [100, 715, 180, 58]   # Ajustamos el botón volver

        # Imagen "Tu puntuación"
        self.score_image_path = "archivos_multimedia/imagenes/tu_puntuacion.png"
        self.score_image_size = (200, 60)  # Tamaño 

        self.score_value = StaticFunctions.score  # Aca iria el score

        # Fuente y colores
        self.font = pygame.font.SysFont("Arial", 30, True, False)
        self.color_active = pygame.Color('dodgerblue2')
        self.color_inactive = pygame.Color('lightskyblue3')

    def init_final_screen(self):
        """
        Inicializa la pantalla final.
        Sincroniza el puntaje final desde StaticFunctions.
        """
        self.score_value = StaticFunctions.score  # *** Actualiza el puntaje dinámico del juego ***

        # Dibuja el fondo
        self.screen.blit(self.fondo, (0, 0))
        
        # *** Muestra imagen del puntaje ***
        score_image_size = (400, 100)  
        StaticFunctions.dibujar_imagen(self.screen, self.score_image_path, [360, 250, *score_image_size])

        # Dibuja el puntaje al lado de la imagen
        score_text_position = [700, 265]
        StaticFunctions.dibujar_texto(
            self.screen,
            f"{self.score_value} puntos",
            40, 
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

        # Botones
        submit_button_path = "archivos_multimedia/imagenes/boton_guardar.png"
        back_button_path = "archivos_multimedia/imagenes/boton_volver.png"
        StaticFunctions.dibujar_imagen(self.screen, submit_button_path, self.submit_button)
        StaticFunctions.dibujar_imagen(self.screen, back_button_path, self.button_back)

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

                if pygame.Rect(*self.submit_button).collidepoint(event.pos):
                    if self.name:
                        print("Nombre ingresado:", self.name)
                        print("Puntuación enviada:", (self.score_value))
                        StaticFunctions.guardar_puntaje(self.name, self.score_value)
                        StaticFunctions.current_screen = "Menu"  # Regresa al menú principal


                if pygame.Rect(*self.button_back).collidepoint(event.pos):
                    print("Volviendo al menú principal...")
                    StaticFunctions.current_screen = "Menu"  # Regresa al menú principal

            # Manejo de teclado
            if event.type == pygame.KEYDOWN and self.input_active:
                if event.key == pygame.K_RETURN:
                    if self.name:
                        StaticFunctions.guardar_puntaje(self.name, self.score_value)  
                        StaticFunctions.current_screen = "Menu"  

                elif event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]
                else:
                    if event.unicode.isalpha():
                        self.name += event.unicode

        return True
