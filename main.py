import pygame  # Librería principal para crear juegos en 2D
from pathlib import Path  # Para trabajar con rutas de archivos
from configuraciones import *  # Importa configuraciones globales (colores, tamaños, etc.)
from funciones import *  # Importa funciones auxiliares (como gestión de eventos, mostrar texto, etc.)
from colores import *  # Importa colores predefinidos
import time  # Para trabajar con tiempo (aunque no se utiliza en este fragmento)
from pantalla_cargar_preguntas import *  # Importa la pantalla para cargar preguntas
from pantalla_easter_egg import *  # Importa la pantalla del easter egg
from pantalla_jugar import *  # Importa la pantalla de juego
from pantalla_menu import *  # Importa la pantalla del menú principal
from pantalla_top import *  # Importa la pantalla de los tops mundiales
from ruleta import *

# Inicializar Pygame
pygame.init()  # Inicializa los módulos de Pygame
pygame.mixer.init()  # Inicializa el mezclador de sonido de Pygame
pygame.font.init()  # Inicializa los módulos de fuente para renderizar texto

# Cargar icono
icono = pygame.image.load('assets/preguntados.jpg')  # Carga el icono de la aplicación
pygame.display.set_icon(icono)  # Establece el icono para la ventana del juego

# Texto de arriba
pygame.display.set_caption("Menu preguntados!")  # Establece el título de la ventana del juego

# Pantalla principal y fondo
pantalla = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Crea la ventana del juego
ruta_fondo = "assets/fondo.jpg"  # Ruta a la imagen de fondo
imagen_fondo = pygame.image.load(ruta_fondo)  # Carga la imagen de fondo
imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (800, 600))  # Escala la imagen de fondo a 800x600

# Opciones de menú
jugar = True  # Variable de control del bucle principal
estado = "menu"  # Estado inicial del juego. Puede ser "menu", "juego", "Ver top mundiales" o "entrando preguntas"

# Variables globales
cuadros_texto = ["", "", "", "", ""]  # Los 5 cuadros de texto vacíos para las preguntas y respuestas
cuadro_activo = 0  # El primer cuadro es el activo
reloj = pygame.time.Clock()  # Objeto para controlar la tasa de refresco (FPS)

# Variables para las preguntas
pregunta_actual_index = 0  # Índice de la pregunta actual
# tema_elegido = 'Autos'

# Bucle principal
while jugar:
    pos_mouse = pygame.mouse.get_pos()  # Obtiene la posición actual del mouse

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugar = False  # Termina el juego si se cierra la ventana

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos  # Obtiene la posición del clic del mouse

            # Estando en el menú
            if estado == "menu":
                # Detectar clics en los botones del menú
                if 300 <= pos[0] <= 500 and 100 <= pos[1] <= 150:
                    estado = "juego"  # Cambia a estado de "juego"
                elif 300 <= pos[0] <= 500 and 200 <= pos[1] <= 250:
                    estado = "Ver top mundiales"  # Cambia a estado de "Ver top mundiales"
                elif 700 <= pos[0] <= 740 and 550 <= pos[1] <= 580:
                    jugar = False  # Sale del juego si se hace clic en "Salir"
                elif 300 <= pos[0] <= 500 and 300 <= pos[1] <= 350:
                    estado = "agregar preguntas"  # Cambia a estado de "agregar preguntas"
                elif 600 <= pos[0] <= 680 and 550 <= pos[1] <= 580:
                    print("y esto?")  # Muestra un mensaje para un caso especial en el menú
                    estado = "o.O"  # Cambia a estado de easter egg
                    
            # Estando en "agregar preguntas"
            elif estado == "agregar preguntas":
                dibujar_boton_volver_preguntas = dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto)
                if dibujar_boton_volver_preguntas.collidepoint(pos):
                    estado = "menu"

            elif estado == "o.O":
                dibujar_boton_volver_gatitos = easter_egg(pantalla, pos_mouse)
                if dibujar_boton_volver_gatitos.collidepoint(pos):
                    estado = "menu"
            
            elif estado == "juego":
                pantalla.blit(imagen_fondo_escalar, (0, 0))
                if True:
                    if tema_elegido == '':
                        tema_elegido = jugar_ruleta()  # Tema elegido
                        tema_elegido = tema_elegido[1]
                        preguntas = cargar_preguntas(elegir_tema(tema_elegido))
                        botones =  mostrar_preguntas(pantalla, preguntas, pregunta_actual_index)
                        
                    elif tema_elegido == 'Autos':
                        preguntas = cargar_preguntas(elegir_tema(tema_elegido))
                        botones =  mostrar_preguntas(pantalla, preguntas, pregunta_actual_index)
                            
                    elif tema_elegido == 'Television':
                        preguntas = cargar_preguntas(elegir_tema(tema_elegido))
                        botones = mostrar_preguntas(pantalla, preguntas, pregunta_actual_index)

                    elif tema_elegido == 'Preguntas_Cargadas':
                        preguntas = cargar_preguntas(elegir_tema(tema_elegido))
                        botones = mostrar_preguntas(pantalla, preguntas, pregunta_actual_index)
                            
                    elif tema_elegido == 'Juegos':
                        preguntas = cargar_preguntas(elegir_tema(tema_elegido))
                        botones = mostrar_preguntas(pantalla, preguntas, pregunta_actual_index)

            
            elif estado == "Ver top mundiales":
                dibujar_boton_volver_top = dibujar_botones_top_mundial(pantalla, pos_mouse)
                if dibujar_boton_volver_top.collidepoint(pos):
                    estado = "menu"
                    
        if estado == "agregar preguntas":
            cuadro_activo, cuadros_texto = gestionar_eventos_entrada(evento, cuadro_activo, cuadros_texto)  # Actualiza la entrada de texto
            
    # Redibujar pantalla según el estado
    pantalla.fill(BLACK)  # Rellena la pantalla con un color negro

    if estado == "menu":
        pantalla.blit(imagen_fondo_escalar, (0, 0))  # Dibuja el fondo en el estado "menu"
        botones_menu = dibujar_menu_botones(pantalla, pos_mouse)  # Dibuja los botones del menú
        tema_elegido = ''

    elif estado == "juego":
        
        if tema_elegido != '':
            botones = mostrar_preguntas(pantalla, preguntas, pregunta_actual_index)
        # Detectar clic en las respuestas
            for i, boton in enumerate(botones):
                if boton.collidepoint(pos):  # Si el clic está dentro de un botón de respuesta
                    pregunta_actual_index += 1  # Avanzar a la siguiente pregunta
                if pregunta_actual_index >= len(preguntas):
                    estado = "menu"
                    
    elif estado == "Ver top mundiales":
        pantalla.blit(imagen_fondo_escalar, (0, 0))
        botones_tops_mundiales = dibujar_botones_top_mundial(pantalla, pos_mouse)  # Dibuja los botones para ver el top mundial
        #mostrar_ranking()
    
    elif estado == "agregar preguntas":
        pantalla.blit(imagen_fondo_escalar, (0, 0))
        dibujar_boton_volver_preguntas = dibujar_botones_agregar_pregunta(pantalla, pos_mouse, cuadro_activo, cuadros_texto)
        
    elif estado == "o.O":
        dibujar_boton_volver_gatitos = easter_egg(pantalla, pos_mouse)

    # Actualización de la pantalla
    pygame.display.update()  # Actualiza la pantalla con los cambios realizados

    # Control de FPS
    reloj.tick(30)  # Limita la tasa de refresco a 30 FPS

pygame.quit()  # Finaliza Pygame y cierra la ventana
