from pathlib import Path  # Para trabajar con rutas de archivos

import pygame  # Libreria principal para crear juegos en 2D
from pygame import \
    surface  # Importa la clase 'surface' de pygame para trabajar con superficies (pantallas)

from colores import *  # Importa los colores definidos en otro archivo
from configuraciones import *  # Importa configuraciones (posiblemente con mas valores de colores, configuraciones de juego, etc.)


# Funcion para dibujar botones con texto en un fondo transparente, con deteccion de hover (cuando el mouse pasa sobre ellos)
def dibujar_texto_con_boton_transparente(pantalla:surface, texto, x:int, y:int, ancho:int, alto:int, color_normal:tuple, color_hover:tuple, pos_mouse):
    ''' 
    ¿Para qua sirve?
    Dibuja un boton con texto que cambia de color cuando el mouse pasa por encima (hover).

    ¿Qua parametro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibuja el boton.
    - texto: (str) El texto que se mostrara en el boton.
    - x: (int) La posicion en el eje X de la esquina superior izquierda del boton.
    - y: (int) La posicion en el eje Y de la esquina superior izquierda del boton.
    - ancho: (int) El ancho del boton.
    - alto: (int) El alto del boton.
    - color_normal: (tuple) El color del texto cuando no hay hover.
    - color_hover: (tuple) El color del texto cuando el mouse esta encima del boton.
    - pos_mouse: (tuple) Las coordenadas actuales del mouse.

    ¿Qua retorna?
    - pygame.Surface: El texto renderizado, que actua como el "boton" visual.
    '''
    
    pos_mouse = pygame.mouse.get_pos()  # Obtiene la posicion del mouse
    color_texto = color_hover if x <= pos_mouse[0] <= x + ancho and y <= pos_mouse[1] <= y + alto else color_normal  # Cambia el color si el mouse esta sobre el boton
    fuente = pygame.font.SysFont("Showcard Gothic", 30)  # Selecciona la fuente
    texto_renderizado = fuente.render(str(texto), True, color_texto)  # Renderiza el texto con el color adecuado
    texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))  # Ajusta el rectangulo para centrar el texto en el boton
    mostrar_texto = pantalla.blit(texto_renderizado, texto_rect)  # Dibuja el texto en la pantalla

    return mostrar_texto  # Retorna la superficie con el texto renderizado


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


# Funcion para dibujar los puntos del jugador en la pantalla
def dibujar_puntos(pantalla, puntos):
    '''
    ¿Para qua sirve?
    Esta funcion dibuja el puntaje del jugador en la pantalla.

    ¿Qua parametro acepta?
    - pantalla: (pygame.Surface) La superficie donde se dibuja el puntaje.
    - puntos: (int) La cantidad de puntos que tiene el jugador.

    ¿Qua retorna?
    - None. La funcion solo dibuja los puntos en la pantalla.
    '''
    fuente = pygame.font.Font(None, 36)  # Crea una fuente con un tamaño de 36
    texto = fuente.render(f"Puntos: {puntos}", True, (BLACK))  # Renderiza el texto con los puntos
    pantalla.blit(texto, (600, 10))  # Dibuja el texto en la pantalla

# Funcion para mostrar texto en la pantalla
def mostrar_texto(texto, superficie, x, y, color=BLACK, font_size=30):
    ''' 
    ¿Para qua sirve?
    Esta funcion permite mostrar un texto en una superficie de Pygame en una posicion especifica.

    ¿Qua parametro acepta?
    - texto: (str) El texto que se va a mostrar en la pantalla.
    - superficie: (pygame.Surface) La superficie sobre la cual se dibuja el texto.
    - x: (int) La posicion en el eje X donde se dibujara el texto.
    - y: (int) La posicion en el eje Y donde se dibujara el texto.
    - color: (tuple) El color del texto. Por defecto es BLACK.
    - font_size: (int) El tamaño de la fuente del texto. Por defecto es 30.

    ¿Qua retorna?
    - None. La funcion solo dibuja el texto en la pantalla sin devolver nada.
    '''
    fuente = pygame.font.Font(None, font_size)  # Crea un objeto fuente con el tamaño especificado
    texto_renderizado = fuente.render(texto, True, color)  # Renderiza el texto con la fuente y el color
    superficie.blit(texto_renderizado, (x, y))  # Dibuja el texto en la superficie en la posicion (x, y)
    

# Función para mostrar un cartel
def mostrar_cartel(screen, texto, duracion, color_fondo, color_texto):
    """
    Muestra un cartel en la pantalla durante un tiempo específico.

    Parámetros:
    - screen: La superficie de Pygame donde se dibuja el cartel.
    - texto: El texto a mostrar.
    - duracion: Duración en segundos que el cartel estará visible.
    - font: Fuente para el texto.
    - color_fondo: Color de fondo de la pantalla.
    - color_texto: Color del texto.
    """
    inicio = pygame.time.get_ticks()  # Tiempo actual en milisegundos
    fuente = pygame.font.Font(None, 36)
    while True:
        tiempo_actual = pygame.time.get_ticks()

        # Dibujar el fondo y el texto
        screen.fill(color_fondo)
        texto_renderizado = fuente.render(texto, True, color_texto)
        screen.blit(texto_renderizado, ((800 - texto_renderizado.get_width()) // 2, (600 - texto_renderizado.get_height()) // 2))

        # Actualizar pantalla
        pygame.display.flip()

        # Salir del bucle después de la duración especificada
        if tiempo_actual - inicio >= duracion * 1000:
            break