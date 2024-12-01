import pygame  # Importa la libreria Pygame para crear el juego.
from pathlib import Path  # Para trabajar con rutas de archivos
from configuraciones import *  # Importa configuraciones globales como colores y tamaños (archivo externo).
from funciones import *  # Importa funciones auxiliares, por ejemplo para manejar eventos o mostrar texto (archivo externo).
from colores import *  # Importa colores predefinidos para usar en el juego (archivo externo).
from pantalla_cargar_preguntas import *  # Importa la pantalla para cargar preguntas (archivo externo).
from pantalla_easter_egg import *  # Importa la pantalla del easter egg (archivo externo).
from pantalla_jugar import *  # Importa la pantalla de juego (archivo externo).
from pantalla_menu import *  # Importa la pantalla del menu principal (archivo externo).
from pantalla_top import *  # Importa la pantalla para mostrar el top mundial (archivo externo).
from ruleta import *  # Importa funciones para la ruleta (archivo externo).
from funciones_preguntas import *  #Importa funciones relacionadas con las preguntas (archivo externo).
from pantalla_config import *

# Inicializar Pygame
pygame.init()  # Inicializa todos los modulos necesarios para usar Pygame.
pygame.mixer.init()  # Inicializa el mezclador de sonidos (para reproducir musica y efectos de sonido).
pygame.font.init()  # Inicializa el sistema de fuentes para poder renderizar texto.

# Cargar sonido de fondo
sonido = pygame.mixer.Sound('assets/musicaa.mp3')  # Carga el archivo de musica.
sonido.set_volume(0.1)  # Establece el volumen a 0.1.
sonido.play()  # Reproduce la musica en bucle.

# Crear la ventana del juego
pantalla = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Configura la pantalla con tamaño 800x600 (redimensionable).

# Cargar imagenes
corazon_lleno = pygame.image.load("assets/corazon_lleno.png")  # Carga la imagen del corazon lleno.
imagen_fondo = pygame.image.load("assets/fondo.jpg")  # Carga la imagen de fondo.
icono = pygame.image.load('assets/preguntados.jpg')  # Carga el icono de la aplicacion.
Titulo = pygame.image.load('assets/titulo.png')  # Carga la imagen del titulo.

# Configuracion de la ventana
pygame.display.set_icon(icono)  # Establece el icono para la ventana del juego.


# Pantalla principal y fondo
imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (800, 600))  # Redimensiona la imagen de fondo a 800x600.
Titulo_escalado = pygame.transform.scale(Titulo, (200, 80))  # Redimensiona la imagen del titulo.
corazon_lleno_escalado = pygame.transform.scale(corazon_lleno, (20, 20))  # Redimensiona la imagen del corazon.

# Variables de control del juego
jugar = True  # Variable de control para el bucle principal del juego.
estado = "menu"  # Estado inicial del juego (en el menu principal).

# Variables globales para las preguntas
preguntas_guardadas = []  # Lista de preguntas guardadas
path_csv_cargar = Path('preguntas_cargadas.csv')  # Archivo donde se guardan las preguntas
cuadro_activo = 0  # indice del cuadro activo (inicia en 0)
cuadros_texto = ["", "", "", "", ""]  # Lista de cuadros de texto (pregunta y respuestas)

path_csv = Path('ranking_top.csv')

reloj = pygame.time.Clock()  # Crea un reloj para controlar los FPS.

# Variables para las preguntas
pregunta_actual_index = 0  # indice de la pregunta actual.

bandera_click = False  # Bandera para detectar si se hizo un clic.

# Bucle principal del juego
puntos = 0  # Inicializa los puntos del jugador.
pos = [0, 0]  # Posicion del mouse (inicializada en [0, 0]).

guardado = False

bandera_juego = False

# Bucle principal donde ocurre todo
while jugar:
    pos_mouse = pygame.mouse.get_pos()  # Obtiene la posicion del mouse.

    for evento in pygame.event.get():  # Maneja los eventos del juego (como clics y cierre de ventana).
        if evento.type == pygame.QUIT:
            jugar = False  # Termina el juego si se cierra la ventana.

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos  # Obtiene la posicion del clic del mouse.
            bandera_click = True  # Marca que se hizo un clic.

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
            elif 700 <= pos[0] <= 800 and 550 <= pos[1] <= 600:
                estado = "configuracion"
            elif 600 <= pos[0] <= 50 and 550 <= pos[1] <= 580:
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
            mostrar_top(pantalla, path_csv)
            if dibujar_boton_volver_top.collidepoint(pos):
                estado = "menu"
                
        # Estando en "agregar preguntas"
        elif estado == "agregar preguntas":
            pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo.
            dibujar_boton_volver_preguntas = dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto)  # Dibuja los botones para agregar preguntas.
            cuadro_activo, cuadros_texto = gestionar_eventos_entrada(evento, cuadro_activo, cuadros_texto)
            if dibujar_boton_volver_preguntas.collidepoint(pos):
                estado = "menu"
                
        elif estado == "configuracion":
            pantalla.blit(imagen_fondo_escalar, (0, 0))
            dibujar_boton_volver_config = dibujar_botones_config(pantalla, pos_mouse)
            if dibujar_boton_volver_config.collidepoint(pos):
                estado = "menu"
            
        # Estando en el easter egg
        elif estado == "o.O":
            dibujar_boton_volver_gatitos = easter_egg(pantalla, pos_mouse)
            if dibujar_boton_volver_gatitos.collidepoint(pos):
                estado = "menu"  # Vuelve al menu principal.
        
    # Redibujar la pantalla segun el estado
    pantalla.fill(CYAN3)  # Rellena la pantalla con el color CYAN3.

    if estado == "menu":
        pygame.display.set_caption("Menu preguntados!")
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo del menu.
        botones_menu = dibujar_menu_botones(pantalla, pos_mouse)  # Dibuja los botones del menu.
        pantalla.blit(Titulo_escalado, (300, 20))  # Dibuja el titulo escalado en la pantalla.
        tema_elegido = ''  # Reinicia el tema.
        vidas = 3  # Reinicia las vidas.
        if bandera_juego == True:
            print(f"tus puntos fueron {puntos}")
            puntos = 0
            bandera_juego = False

        
    elif estado == "juego":
        pygame.display.set_caption("Vamos a jugar")
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo en el juego.
        if tema_elegido != '':  # Si ya se eligio un tema.
            bandera_juego = True
            botones, pregunta_actual_index, respuestas, vidas_vis = mostrar_preguntas(pantalla, preguntas, pregunta_actual_index, pos_mouse, vidas)  # Muestra las preguntas.

            for i, boton in enumerate(botones):
                if boton.collidepoint(pos) and bandera_click:  # Si se hace clic en una respuesta.
                    pregunta = preguntas[pregunta_actual_index]
                    respuestas = pregunta[1:]  # Las respuestas estan en los indices 1 y siguientes.
                    
                    respueta_elegida = respuestas[i]
                    respuesta_correcta = pregunta[-1]  # La ultima respuesta es la correcta.
                    
                    if respueta_elegida == respuesta_correcta:
                        puntos += 1  # Suma un punto si la respuesta es correcta.
                    else:
                        vidas -= 1  # Resta una vida si la respuesta es incorrecta.
                        
                    pregunta_actual_index += 1  # Avanza al siguiente indice de la pregunta.
            dibujar_puntos(pantalla, puntos)  # Muestra los puntos en la pantalla.
                    
            if vidas == 0 or pregunta_actual_index >= len(preguntas):  # Si las vidas llegan a 0, vuelve al menu o Si ya no hay preguntas, vuelve al menu.
                estado = "menu" 
        
    elif estado == "Ver top mundiales":
        pygame.display.set_caption("Vamos a ver los tops!")
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo.
        botones_tops_mundiales = dibujar_botones_top_mundial(pantalla, pos_mouse)  # Dibuja los botones para el top mundial.
        mostrar_top(pantalla, path_csv)
        
    elif estado == "agregar preguntas":
        pygame.display.set_caption("Agregar preguntas!")
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo.
        dibujar_boton_volver_preguntas = dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto)  # Dibuja los botones para agregar preguntas.
        if guardado == False:
            guardar_textos(cuadros_texto, path_csv_cargar)
            guardado = True
    
    elif estado == "configuracion":
        pantalla.blit(imagen_fondo_escalar, (0, 0))
        dibujar_boton_volver_config = dibujar_botones_config(pantalla, pos_mouse)


    elif estado == "o.O":
        dibujar_boton_volver_gatitos = easter_egg(pantalla, pos_mouse)  # Dibuja la pantalla del easter egg.
        
    # Actualizar la pantalla
    bandera_click = False  # Resetea la bandera del clic.
    pygame.display.update()  # Actualiza la pantalla.

    # Control de FPS
    reloj.tick(60)  # Limita la tasa de refresco a 60 FPS.

# Termina el juego y cierra la ventana.
pygame.quit()
