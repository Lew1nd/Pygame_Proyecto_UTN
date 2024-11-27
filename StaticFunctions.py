'''
Aquí estarán las funciones y objetos que pueden estar presentes en varias pantallas a la vez
'''
import pygame
import csv
import random
current_screen = ""
change_screen_flag = True
WIDTH, HEIGHT = 1280,800

#Atributos del jugador
lives = 3
timer = 30#Variable usada para el timer
time_config = 30#Variable para mostrar el tiempo configurado en pantalla
score_gain_per_question = 1

#Gestionador de preguntas y respuestas
questions = ["Ingrese su pregunta aquí", 
             "Ingrese una posible respuesta aquí", 
             "Ingrese una posible respuesta aquí", 
             "Ingrese una posible respuesta aquí",
             "Ingrese la respuesta correcta aquí"]#5

selected_category = "Anime"
selected_difficulty = "Fácil"

questions_datapath = "archivos_multimedia/preguntas.csv"#Ubicación del archivo preguntas
player_datapath = "archivos_multimedia/playerdata.csv"#Ubicación del archivo de playerdata

#Juego
difficulty_game = ""
category_game = ""
score = 4
all_questions_data = []

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
        text_list[:] = [False] * len(text_list)#Toma todos los elementos de la lista y los vuelve False
        text_list[selected_text] = True#Vuelve true el que recibió como parámetro

def texto_vacio(text_list: list, string: str, selected_text: int):
        '''
        Comprueba si el usuario dejó vacío el texto.
        Recibe la cadena, y el índice de la cadena de texto que se está modificando
        No devuelve nada
        '''
        if string == "": text_list[selected_text] = True
        else: text_list[selected_text] = False

def mostrar_timer(surface, color, seg : int, position):
    '''
    Dibuja un temporizador en la pantalla.
    Recibe la superficie de la pantalla, color, segundos y las coordenadas de la pantalla.
    No devuelve nada.
    '''
    fuente = pygame.font.Font(None, 48)
    contador_seg = seg
    mensaje_tiempo = f"{str(contador_seg).zfill(2)}"
    texto = fuente.render(mensaje_tiempo, True, color)
    surface.blit(texto, (position))

def cargar_datos(datapath, data: str):
    '''
    Función encargada de leer archivos.\n
    Recibe la ubicación del archivo a leer, data funciona como filtro para leer un archivo en concreto.\n
    No devuelve nada.
    '''
    def cargar_datos_jugador(archive):
        '''
        Obtiene el contenido del arhicov playerdata.scv.\n
        Recibe el archivo leido.\n
        No devuelve nada.
        '''
        global timer, lives, score_gain_per_question, time_config
        content = archive.readlines()
        player_data = content[0].replace('\n','').split(',')

        time_config = int(player_data[0])
        lives = int(player_data[1])
        score_gain_per_question = int(player_data[2])
        timer = time_config
    
    def obtener_preguntas_filtradas(archive):
        '''
        Obtiene todas las preguntas por la categoría y dificultad seleccionadas\n.
        Recibe el archivo leido\n.
        No devuelve nada.
        '''
        global all_questions_data, category_game, difficulty_game
        content = csv.DictReader(archive)
        for question in content:
            if question["Categoría"] == category_game and question["Dificultad"] == difficulty_game: all_questions_data.append(question)
                
    with open(datapath, 'r', encoding="utf-8") as archivo:
        match data:
            case "Player": cargar_datos_jugador(archivo)
            case "Start": obtener_preguntas_filtradas(archivo)

def guardar_datos(datapath, data: str, operation: str):
    '''
    Permite gestionar diferentes guardados de diferentes archivos.\n
    Recibe la ubicación del archivo, el archivo a modificar (data) y la operación que se va a hacer.\n
    No devuelve nada.
    '''
    def agregar_pregunta_a_archivo(datapath, operation: str):
        '''
        Agrega una pregunta nueva al archivo de preguntas.\n
        Recibe la ubicación del archivo y el tipo de operación que va a hacer.\n
        No devuelve nada.
        '''
        datos = [None] * 8
        preguntas = [""] * 4

        pregunta_correcta = questions[4]
    
        posicion_pregunta_correcta = 4
    
        for i in range(len(preguntas)): 
            preguntas[i] = questions[i+1]
            preguntas_aleatorio = random.sample(preguntas, len(preguntas))
            #Aleatoriza el orden de todos los valores de la lista, y las guarda en una lista nueva

        for i in range(len(preguntas_aleatorio)):
            if pregunta_correcta == preguntas_aleatorio[i]: posicion_pregunta_correcta = i

        datos[0] = questions[0]#Pregunta
        datos[1] = preguntas_aleatorio[0]#Opción A
        datos[2] = preguntas_aleatorio[1]#Opción B
        datos[3] = preguntas_aleatorio[2]#Opción C
        datos[4] = preguntas_aleatorio[3]#Opción D
        datos[5] = int(posicion_pregunta_correcta)#Correcta
        datos[6] = selected_category#Categoría
        datos[7] = selected_difficulty#Dificultad
        with open(datapath, operation, newline='\n', encoding="utf-8") as archivo:
            write_csv = csv.writer(archivo)
            write_csv.writerow([
                datos[0], datos[1], datos[2], datos[3], 
                datos[4], datos[5], datos[6], datos[7],"0","0","0"])
            archivo.close()

    def actualizar_datos_jugador(datapath, operation: str):

        '''
        Actualiza los datos que ingresó el usuario.\n
        Recibe la ubicación del archivo y el tipo de operación que realizará.\n
        No devuelve nada
        '''
        datos = [0] * 3
        datos[0] = time_config
        datos[1] = lives
        datos[2] = score_gain_per_question
        with open(datapath, operation) as archivo:
            write_csv = csv.writer(archivo)
            write_csv.writerow([datos[0], datos[1], datos[2]])
            print(datos)
            archivo.close()

    match data:
        case "Question_add": agregar_pregunta_a_archivo(datapath, operation)
        case "Player": actualizar_datos_jugador(datapath, operation)

def guardar_puntaje(nombre, puntaje):
        """
        Guarda el nombre y puntaje en el archivo scoreboard.csv.
        Crea el archivo si no existe.
        """
        print(f"Guardando puntaje: Nombre = {nombre}, Puntaje = {puntaje}")  # Depuración
        filepath = "archivos_multimedia/scoreboard.csv"
        with open(filepath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, puntaje])
            
def generar_rectangulo_estilizado(surface, color, dimensiones, borde_color, grosor_borde, redondeo=10):
    """
    Genera y dibuja un rectángulo estilizado con bordes redondeados.
    - surface: Superficie donde se dibujará.
    - color: Color del fondo del rectángulo.
    - dimensiones: Lista [x, y, ancho, alto] del rectángulo.
    - borde_color: Color del borde.
    - grosor_borde: Grosor del borde.
    - redondeo: Redondeo de las esquinas.
    Devuelve el objeto Rect generado.
    """
    # Dibujar el borde
    pygame.draw.rect(surface, borde_color, dimensiones, border_radius=redondeo)
    
    # Dibujar el rectángulo interior
    x, y, ancho, alto = dimensiones
    pygame.draw.rect(
        surface, 
        color, 
        [x + grosor_borde, y + grosor_borde, ancho - 2 * grosor_borde, alto - 2 * grosor_borde], 
        border_radius=redondeo
    )
    
    return pygame.Rect(dimensiones)

def dibujar_texto_estilizado(superficie, texto, tamano, color, posicion, centrado_horizontal=True, centrado_vertical=True, fuente="Arial", negrita=False, fuente_archivo=None):
    """
    Dibuja texto estilizado en la superficie con opciones de tamaño, color, fuente y alineación.
    Divide el texto en líneas si excede el ancho del rectángulo especificado.
    """
    if fuente_archivo:
        fuente_obj = pygame.font.Font(fuente_archivo, tamano)
    else:
        fuente_obj = pygame.font.SysFont(fuente, tamano, bold=negrita)
    if isinstance(posicion, tuple):  # Si se da una posición directa (x, y)
        texto_rect = pygame.Rect(posicion[0], posicion[1], 800, 100)  # Rectángulo ficticio con ancho y alto arbitrarios
    else:
        texto_rect = pygame.Rect(posicion)  # Si se da un rectángulo, úsalo directamente
    palabras = texto.split(' ')  # se divide el texto en palabras
    lineas = []  # se almacenan las líneas generadas
    linea_actual = ''

    # Secrean líneas que entran dentro del ancho 
    for palabra in palabras:
        if fuente_obj.size(linea_actual + palabra)[0] <= texto_rect.width:
            linea_actual += palabra + ' '
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + ' '

    if linea_actual:
        lineas.append(linea_actual.strip())  # se añade la ultima linea

    # Calcula la altura total necesaria
    altura_total = len(lineas) * fuente_obj.get_height()
    offset_y = texto_rect.y

    if centrado_vertical:
        offset_y += (texto_rect.height - altura_total) // 2  # Ajusta verticalmente si se requiere

    # Dibuja cada línea
    for linea in lineas:
        texto_superficie = fuente_obj.render(linea, True, color)
        linea_rect = texto_superficie.get_rect()

        if centrado_horizontal:
            linea_rect.centerx = texto_rect.centerx
        else:
            linea_rect.x = texto_rect.x

        linea_rect.y = offset_y
        superficie.blit(texto_superficie, linea_rect)
        offset_y += fuente_obj.get_height()  # Avanza