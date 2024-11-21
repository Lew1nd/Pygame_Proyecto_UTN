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

        self.text_lives, self.text_lives_input = [50,500], [250, 520] 
        self.text_score, self.text_score_input = [50, 300], [680, 320]
        self.text_time, self.text_time_input = [40, 700], [300,720]
        
        self.lives = str(StaticFunctions.lives)
        self.score = str(StaticFunctions.score_gain_per_question)
        self.time = str(StaticFunctions.time)
        
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
                    case 0: self.lives = value_selected
                    case 1: self.score = value_selected
                    case 2: self.time = value_selected

    def init_options(self):
        back_button = StaticFunctions.dibujar_imagen(self.options, "archivos_multimedia/imagenes/boton_atras.png", self.button_back)
        music_button = StaticFunctions.dibujar_imagen(self.options, "archivos_multimedia/imagenes/boton_musica.png", self.button_music)
        questions_button = StaticFunctions.generar_rectangulo(self.options, GREEN, self.button_question)
        
        lives_text = StaticFunctions.dibujar_texto(self.options, "Vidas: ", 70, YELLOW1, self.text_lives, True, False)
        lives_input_text = StaticFunctions.dibujar_texto(self.options, self.lives, 50, RED1, self.text_lives_input, True, False)

        score_text = StaticFunctions.dibujar_texto(self.options, "Puntaje por pregunta: ", 70, YELLOW1, self.text_score, True, False)
        score_input_text = StaticFunctions.dibujar_texto(self.options, self.score, 50, RED1, self.text_score_input, True, False)

        time_text = StaticFunctions.dibujar_texto(self.options, "Tiempo: ", 70, YELLOW1, self.text_time, True, False)
        time_input_text = StaticFunctions.dibujar_texto(self.options, self.time, 50, RED1, self.text_time_input, True, False)

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
                elif lives_input_text.collidepoint(pygame.mouse.get_pos()): StaticFunctions.seleccionar_texto(self.text_focus, 0) 
                elif score_input_text.collidepoint(pygame.mouse.get_pos()): StaticFunctions.seleccionar_texto(self.text_focus,1)
                elif time_input_text.collidepoint(pygame.mouse.get_pos()): StaticFunctions.seleccionar_texto(self.text_focus,2)  
                else:
                    StaticFunctions.texto_vacio(self.text_focus, self.lives, 0)
                    StaticFunctions.texto_vacio(self.text_focus, self.score, 1)
                    StaticFunctions.texto_vacio(self.text_focus, self.time, 2)
                
            self.modificar_texto(event,self.lives,0, 99)
            self.modificar_texto(event,self.score,1, 100000)
            self.modificar_texto(event,self.time,2, 1800)#El parámetro 3 es el tiempo máximo permitido. Ponerlo en segundos
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
        self.answer1 = [50, 200, 550, 50]
        self.answer2 = [50, 300, 550, 50]
        self.answer3 = [50, 400, 550, 50]
        self.answer4 = [50, 500, 550, 50]


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
        #print(StaticFunctions.selected_category)
        #print(StaticFunctions.selected_difficulty)
            
    def init_question_manager(self):
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
                    StaticFunctions.agregar_pregunta_a_archivo()
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
            print(self.text_focus)
            for i in range(len(self.text_focus)):
                self.modificar_texto(event, i-1, i)
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
                    print("Categoria seleccionada: ANIME")   
                elif self.button_games[0] <= pygame.mouse.get_pos()[0] <= self.button_games[0] + self.button_games[2] and \
                     self.button_games[1] <= pygame.mouse.get_pos()[1] <= self.button_games[1] + self.button_games[3]:# Separe elif por lineas para que sea mas legible
                    print("Categoria seleccionada: VIDEOJUEGOS") 
                elif self.button_geography[0] <= pygame.mouse.get_pos()[0] <= self.button_geography[0] + self.button_geography[2] and \
                     self.button_geography[1] <= pygame.mouse.get_pos()[1] <= self.button_geography[1] + self.button_geography[3]:# Separe elif por lineas para que sea mas legible
                    print("Categoria seleccionada: GEOGRAFIA")
                
        return True