from pathlib import Path  # Para trabajar con rutas de archivos

import pygame  # Libreria principal para crear juegos en 2D
from pygame import surface  # Importa la clase 'surface' de pygame para trabajar con superficies (pantallas)

from colores import *  # Importa los colores definidos en otro archivo
from configuraciones import *  # Importa configuraciones (posiblemente con mas valores de colores, configuraciones de juego, etc.)


def dibujar_texto_con_boton_transparente(pantalla: surface, texto: str, x: int, y: int, ancho: int, alto: int, color_normal: tuple, color_hover: tuple, pos_mouse):
    ''' 
    ¿Para qué sirve?
    Dibuja un botón con texto que cambia de color cuando el mouse pasa por encima (hover). 
    Se utiliza para crear botones interactivos en la pantalla.

    ¿Qué parámetros acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibuja el botón (por ejemplo, la pantalla principal del juego).
    - texto: (str) El texto que se mostrará en el botón.
    - x: (int) La posición en el eje X de la esquina superior izquierda del botón.
    - y: (int) La posición en el eje Y de la esquina superior izquierda del botón.
    - ancho: (int) El ancho del botón.
    - alto: (int) El alto del botón.
    - color_normal: (tuple) El color del texto cuando no hay hover (cuando el mouse no está sobre el botón).
    - color_hover: (tuple) El color del texto cuando el mouse está encima del botón (hover).
    - pos_mouse: (tuple) Las coordenadas actuales del mouse en la pantalla.

    ¿Qué retorna?
    - pygame.Surface: El objeto Surface que contiene el texto renderizado, que actúa como el "botón" visual.
    '''
    
    # Obtiene la posición del mouse (actualización de las coordenadas del puntero)
    pos_mouse = pygame.mouse.get_pos()
    
    # Verifica si el mouse está sobre el botón (detección de hover)
    if x <= pos_mouse[0] <= x + ancho and y <= pos_mouse[1] <= y + alto:
        color_texto = color_hover  # Si el mouse está sobre el botón, usa el color hover
    else:
        color_texto = color_normal  # Si el mouse no está sobre el botón, usa el color normal
    
    # Selecciona la fuente para el texto
    fuente = pygame.font.SysFont("Showcard Gothic", 30)
    
    # Renderiza el texto con el color adecuado (normal o hover)
    texto_renderizado = fuente.render(str(texto), True, color_texto)
    
    # Ajusta el rectángulo de la superficie del texto para centrarlo dentro del botón
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))
    
    # Dibuja el texto renderizado en la pantalla en la posición centrada
    mostrar_texto = pantalla.blit(texto_renderizado, texto_rect)
    
    # Retorna la superficie con el texto renderizado, que representa el "botón" visual
    return mostrar_texto



# Funcion para dibujar vidas (corazones) en la pantalla
def dibujar_vidas(pantalla, vidas):
    '''
    ¿Para qua sirve?
    Esta funcion dibuja los corazones que representan las vidas del jugador en la pantalla.

    ¿Qua parametro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibujan los corazones.
    - vidas: (int) La cantidad de vidas que tiene el jugador, se dibuja un corazon por cada vida.

    ¿Qua retorna?
    - None. La funcion solo dibuja los corazones en la pantalla.
    '''
    corazon_lleno = pygame.image.load('assets/corazon_lleno.png')  # Carga la imagen del corazon
    corazon_lleno_escalado = pygame.transform.scale(corazon_lleno, (20, 20))  # Escala la imagen del corazon

    # Posicionar los corazones en la pantalla
    for i in range(vidas):
        pantalla.blit(corazon_lleno_escalado, (50 + i * 50, 30))  # Cada vida se dibuja 50 pixeles a la derecha


# Funcion para mostrar texto en la pantalla
def mostrar_texto(superficie, texto, x=None, y=None, color=BLACK, color_fondo=WHEAT1, font_size=30, permitir_segundos = False, duracion = None): # Por defecto, el texto se muestra en el centro de la pantalla
    ''' 
    ¿Para qué sirve?
    Esta función permite mostrar un texto en una superficie de Pygame en una posición específica. 
    Además, puede mostrar el texto por un tiempo limitado si se activa la funcionalidad de temporizador con `permitir_segundos`.

    ¿Qué parámetros acepta?
    - superficie: (pygame.Surface) La superficie sobre la cual se dibuja el texto.
    - texto: (str) El texto que se va a mostrar en la pantalla.
    - x: (int) La posición en el eje X donde se dibujará el texto. Especificar una posición fija o pasar None para personalizar.
    - y: (int) La posición en el eje Y donde se dibujará el texto. Especificar una posición fija o pasar None para personalizar.
    - color: (tuple) El color del texto. Por defecto es BLACK.
    - fuente: (str) El nombre de la fuente utilizada para el texto. Por defecto es 'Showcard Gothic'.
    - font_size: (int) El tamaño de la fuente del texto. Por defecto es 30.
    - permitir_segundos: (bool) Activa o desactiva el temporizador para mostrar el texto por una duración limitada. Por defecto es False.
    - duracion: (int) Tiempo en segundos durante el cual se muestra el texto si `permitir_segundos` es True. Por defecto es None.

    ¿Qué retorna?
    - None. La función no devuelve ningún valor. Su propósito es dibujar el texto en la pantalla.

    Detalles adicionales:
    - Si `permitir_segundos` es True y se pasa un valor a `duracion`, el texto se mostrará en pantalla durante esa cantidad de segundos antes de desaparecer.
    - Si `permitir_segundos` es False, el texto se dibuja de manera permanente sin temporizador.
    '''
    fuente = pygame.font.Font(None, font_size)  # Crea un objeto fuente con el tamaño especificado
    texto_renderizado = fuente.render(texto, True, color)  # Renderiza el texto con la fuente y el color
    superficie.blit(texto_renderizado, (x, y))  # Dibuja el texto en la superficie en la posicion (x, y)

    if permitir_segundos == True:
        inicio = pygame.time.get_ticks()  # Tiempo actual en milisegundos
        while True:
            tiempo_actual = pygame.time.get_ticks() # Tiempo actual en milisegundos

            # Dibujar el fondo y el texto
            superficie.fill(color_fondo) # Rellena la superficie con un color de fondo
            texto_renderizado = fuente.render(texto, True, color) # Renderiza el texto con la fuente y el color
            superficie.blit(texto_renderizado, ((800 - texto_renderizado.get_width()) // 2, (600 - texto_renderizado.get_height()) // 2)) # Dibuja el texto en el centro de la pantalla

            # Actualizar pantalla
            #pygame.display.flip()

            # Salir del bucle después de la duración especificada
            if tiempo_actual - inicio >= duracion * 1000:
                break

