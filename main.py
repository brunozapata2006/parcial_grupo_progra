from pathlib import Path  # Para trabajar con rutas de archivos

import pygame  # Importa la libreria Pygame para crear el juego.

from colores import *  # Importa colores predefinidos para usar en el juego (archivo externo).
from configuraciones import *  # Importa configuraciones globales como colores y tamaños (archivo externo).
from funciones import *  # Importa funciones auxiliares, por ejemplo para manejar eventos o mostrar texto (archivo externo).
from funciones_dibujar import *
from funciones_preguntas import *  # Importa funciones relacionadas con las preguntas (archivo externo).
from funciones_guardar import *
from pantalla_cargar_preguntas import *  # Importa la pantalla para cargar preguntas (archivo externo).
from pantalla_configuraciones import *
from pantalla_easter_egg import *  # Importa la pantalla del easter egg (archivo externo).
from pantalla_jugar import *  # Importa la pantalla de juego (archivo externo).
from pantalla_menu import *  # Importa la pantalla del menu principal (archivo externo).
from pantalla_top import *  # Importa la pantalla para mostrar el top mundial (archivo externo).
from ruleta import *  # Importa funciones para la ruleta (archivo externo).
from pantalla_configuraciones import * # Importa la pantalla de configuraciones (archivo externo).
from eventos import *
from pantalla_configuraciones import pantalla_configuraciones
from configuraciones  import *

# Inicializar Pygame
pygame.init()  # Inicializa todos los modulos necesarios para usar Pygame.
pygame.mixer.init()  # Inicializa el mezclador de sonidos (para reproducir musica y efectos de sonido).
pygame.font.init()  # Inicializa el sistema de fuentes para poder renderizar texto.

# Cargar sonido de fondo
sonido = pygame.mixer.Sound('assets/musicaa.mp3')  # Carga el archivo de musica.
sonido.set_volume(0)  # Establece el volumen a 0.1.
sonido.play()  # Reproduce la musica en bucle.


# Crear la ventana del juego
pantalla = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Configura la pantalla con tamaño 800x600 (redimensionable).


# Variables de control del juego
jugar = True  # Variable de control para el bucle principal del juego.
estado = "menu"  # Estado inicial del juego (en el menu principal).

# Variables globales para las preguntas
preguntas_guardadas = []  # Lista de preguntas guardadas
path_csv_cargar = Path('preguntas_cargadas.csv')  # Archivo donde se guardan las preguntas
cuadro_activo = 0  # indice del cuadro activo (inicia en 0)
cuadros_texto_config = ["", "", ""]
cuadros_texto_preg = ["", "", "", "", ""]  # Lista de cuadros de texto (pregunta y respuestas)

path_csv_ranking = Path('ranking_top.csv')
path_csv_config = Path('configuracion.csv')

reloj = pygame.time.Clock()  # Crea un reloj para controlar los FPS.

# Variables para las preguntas
pregunta_actual_index = 0  # indice de la pregunta actual.

bandera_click = False  # Bandera para detectar si se hizo un clic.

# Bucle principal del juego
puntos = 0  # Inicializa los puntos del jugador.
pos = [0, 0]  # Posicion del mouse (inicializada en [0, 0]).
#TIEMPO
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # 1 segundo (1000 ms)

# Variables para contar tiempo
segundos_actuales = 0
minutos_actuales = 0


guardado_preg = False
guardado_config = False

bandera_juego = False
configuraciones = abrir_cfg("config.csv")


# Bucle principal donde ocurre todo
while jugar:
    pos_mouse = pygame.mouse.get_pos()  # Obtiene la posicion del mouse
    
    for evento in pygame.event.get():  # Maneja los eventos del juego (como clics y cierre de ventana).
        if evento.type == pygame.QUIT:
            jugar = False  # Termina el juego si se cierra la ventana.
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos  # Obtiene la posicion del clic del mouse.
            bandera_click = True  # Marca que se hizo un clic.
        if evento.type == timer_event:
            segundos_actuales += 1 # Suma un segundo
        if segundos_actuales == 60: # Si pasan 60 segundos
                segundos_actuales = 0 # Reinicia los segundos
                minutos_actuales += 1 # Suma un minuto
                tiempo_en_formato = f"{str(minutos_actuales).zfill(2)}:{str(segundos_actuales).zfill(2)}" # Formato MM:SS
        # Estando en el menu
        if estado == "menu":
            # Detectar clics en los botones del menu
            if 300 <= pos[0] <= 500 and 100 <= pos[1] <= 150:
                estado = "juego"  # Cambia al estado de "juego".
            elif 300 <= pos[0] <= 500 and 200 <= pos[1] <= 250:
                estado = "Ver top mundiales"  # Cambia al estado de "Ver top mundiales".
            elif 700 <= pos[0] <= 740 and 550 <= pos[1] <= 580:
                jugar = False  # Sale del juego si se hace clic en "Salir".
            elif 300 <= pos[0] <= 500 and 300 <= pos[1] <= 350:
                estado = "agregar preguntas"  # Cambia al estado de "agregar preguntas".
            elif 300 <= pos[0] <= 500 and 400 <= pos[1] <= 600:
                estado = "configuracion"
                #300, 400
            elif 50 <= pos[0] <= 100 and 50 <= pos[1] <= 100:
                print("y esto?")
                estado = "o.O" 
        
        # Estando en el estado "juego"
        elif estado == "juego":
            pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo en el juego.
            if tema_elegido == '':  # Si no se ha elegido un tema aun.
                tema_elegido = jugar_ruleta()  # Llama a la funcion para jugar la ruleta y elegir un tema.
                tema_elegido = tema_elegido[1]  # El tema elegido es el segundo elemento del retorno de la ruleta.
            preguntas = cargar_preguntas_desde_csv(elegir_tema(tema_elegido))  # Carga las preguntas segun el tema elegido.
            botones = mostrar_preguntas(pantalla, preguntas, pregunta_actual_index, pos_mouse, vidas)  # Muestra las preguntas y los botones de respuestas.

            if pregunta_actual_index >= len(preguntas):  # Si ya no hay mas preguntas, vuelve al inicio.
                pregunta_actual_index = 0
                
        # Estando en "Ver top mundiales"
        elif estado == "Ver top mundiales":
            dibujar_boton_volver_top = dibujar_botones_top_mundial(pantalla, pos_mouse)  # Dibuja los botones del top mundial.
            mostrar_top(pantalla, path_csv_ranking)
            if dibujar_boton_volver_top.collidepoint(pos):
                estado = "menu"
                
        # Estando en "agregar preguntas"
        elif estado == "agregar preguntas":
            pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo.
            dibujar_boton_volver_preguntas = dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto_preg)  # Dibuja los botones para agregar preguntas.
            cuadro_activo, cuadros_texto_preg = eventos_carg_preguntas(path_csv_cargar, evento, cuadro_activo, cuadros_texto_preg) # Maneja los eventos de los cuadros de texto.
            if dibujar_boton_volver_preguntas.collidepoint(pos):
                estado = "menu" # Vuelve al menu principal.
                
        elif estado == "configuracion":
            nuevo_estado = pantalla_configuraciones(pantalla, pos_mouse, "config.csv") # Muestra la pantalla de configuraciones.
            if nuevo_estado == "menu": # Si se hace clic en "Volver al Menu".
                estado = "menu" # Vuelve al menu principal.
                
             
            
        # Estando en el easter egg
        elif estado == "o.O":
            dibujar_boton_volver_gatitos = easter_egg(pantalla, pos_mouse) # Dibuja la pantalla del easter egg.
            if dibujar_boton_volver_config.collidepoint(pos): # Si se hace clic en "Volver al Menu".
                estado = "menu"
        
    # Redibujar la pantalla segun el estado
    pantalla.fill(BLACK)  # Rellena la pantalla con el color BLACK.

    if estado == "menu":
        pygame.display.set_caption("Menu preguntados!") # Establece el titulo de la ventana.
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo del menu.
        botones_menu = dibujar_menu_botones(pantalla, pos_mouse)  # Dibuja los botones del menu.
        pantalla.blit(Titulo_escalado, (300, 20))  # Dibuja el titulo escalado en la pantalla.
        tema_elegido = ''  # Reinicia el tema.
        vidas = 3  # Reinicia las vidas.
        if bandera_juego == True:
            pantalla.blit(imagen_fondo_escalar, (0, 0)) # Dibuja el fondo en el juego.
            nombre = ingreso_nombre(pantalla, pos_mouse) # Pide el nombre del jugador.
            guardar_nombre_csv(nombre, puntos, path_csv_ranking) # Guarda el nombre y los puntos en el ranking.
            puntos = 0 # Reinicia los puntos.
            bandera_juego = False # Reinicia la bandera del juego.

    elif estado == "juego":
        pygame.display.set_caption("Vamos a jugar") # Establece el titulo de la ventana.
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo en el juego.
        if tema_elegido != '':  # Si ya se eligio un tema.
            bandera_juego = True
            botones, pregunta_actual_index, respuestas, vidas_vis = mostrar_preguntas(pantalla, preguntas, pregunta_actual_index, pos_mouse, vidas)  # Muestra las preguntas.

            for i, boton in enumerate(botones):
                if boton.collidepoint(pos) and bandera_click:  # Si se hace clic en una respuesta.
                    pregunta = preguntas[pregunta_actual_index] # Obtiene la pregunta actual.
                    respuestas = pregunta[1:]  # Las respuestas estan en los indices 1 y siguientes.
                    
                    respueta_elegida = respuestas[i] # La respuesta elegida es la que corresponde al indice del boton.
                    respuesta_correcta = pregunta[-1]  # La ultima respuesta es la correcta.
                    
                    if respueta_elegida == respuesta_correcta:
                        puntos += punto  # Suma un punto si la respuesta es correcta.
                    else:
                        vidas -= 1  # Resta una vida si la respuesta es incorrecta.
                        if vidas == 2:
                            mostrar_texto(pantalla, "Tienes 2 vidas",400, 300, permitir_segundos=True, duracion=1)   # Muestra un mensaje si quedan 2 vidas.        
                        if vidas == 1:
                            mostrar_texto(pantalla, "Tienes 1 vida",400, 300, permitir_segundos=True, duracion=1)  # Muestra un mensaje si queda 1 vida.

                    dibujar_texto_con_boton_transparente(pantalla,segundos_actuales, 300,300, 100,100, RED1, RED1,pos_mouse) # Muestra el tiempo en pantalla
                    pregunta_actual_index += 1  # Avanza al siguiente indice de la pregunta.
            mostrar_texto(pantalla, f"Puntos: {puntos}",(600), (10))  # Muestra los puntos en la pantalla.

            if vidas == 0 or pregunta_actual_index >= len(preguntas):  # Si las vidas llegan a 0, vuelve al menu o Si ya no hay preguntas, vuelve al menu
                estado = "menu" 
        
    elif estado == "Ver top mundiales":
        pygame.display.set_caption("Vamos a ver los tops!") # Establece el titulo de la ventana.
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo.
        botones_tops_mundiales = dibujar_botones_top_mundial(pantalla, pos_mouse)  # Dibuja los botones para el top mundial.
        mostrar_top(pantalla, path_csv_ranking) # Muestra el top mundial.
        
    elif estado == "agregar preguntas":
        pygame.display.set_caption("Agregar preguntas!") # Establece el titulo de la ventana.
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo.
        dibujar_boton_volver_preguntas = dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto_preg)  # Dibuja los botones para agregar preguntas.
        if guardado_preg == False: # Si no se han guardado las preguntas.
            guardar_textos(cuadros_texto_preg, path_csv_cargar) # Guarda las preguntas en el archivo.
            guardado_preg = True # Marca que ya se guardaron las preguntas.
     
    elif estado == "configuracion": # Si se esta en la pantalla de configuraciones
        pantalla.blit(imagen_fondo_escalar, (0, 0)) # Dibuja el fondo.
        boton_volver_menu_config, boton_guardar = dibujar_botones_configuraciones(pantalla, pos_mouse, cuadro_activo, cuadros_texto_config) # Dibuja los botones y cuadros de texto.
        dibujar_boton_volver_config = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse) # Dibuja el boton "Volver al Menu".
        if guardado_config == False: # Si no se ha guardado la configuracion.
            guardar_cfg(cuadros_texto_config[0], cuadros_texto_config[1], cuadros_texto_config[2], "config.csv") # Guarda la configuracion en el archivo.
            guardado_config = True # Marca que ya se guardo la configuracion.

    elif estado == "o.O":
        dibujar_boton_volver_gatitos = easter_egg(pantalla, pos_mouse)  # Dibuja la pantalla del easter egg.
        
    # Actualizar la pantalla
    bandera_click = False  # Resetea la bandera del clic.
    pygame.display.update()  # Actualiza la pantalla.

    # Control de FPS
    reloj.tick(60)  # Limita la tasa de refresco a 60 FPS.

# Termina el juego y cierra la ventana.
pygame.quit()
