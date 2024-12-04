import random
import sys

import pygame

from funciones_eventos import *
from funciones_dibujar import *


def jugar_ruleta():
    '''
    Plantilla Documentacion
    ¿Para qua sirve?
    Esta funcion gestiona un juego de ruleta giratoria en Pygame. El jugador puede hacer clic en la ruleta para hacerla girar, y luego se detiene mostrando un tema aleatorio basado en la posicion de la ruleta.

    ¿Qua parámetro acepta?
    - Ninguno.

    ¿Qua retorna?
    - fondo: (Surface) La superficie del fondo renderizada.
    - tema_final: (str) El tema seleccionado aleatoriamente en base a la posicion de la ruleta.
    '''
    bandera_girada = False # Bandera para mostrar el tema solo una vez
    # Configuracion inicial
    pygame.init()
    ALTO, ANCHO = 800, 600 # Tamaño de la ventana
    pantalla = pygame.display.set_mode((ALTO, ANCHO), pygame.RESIZABLE) # Crear ventana
    pygame.display.set_caption("Ruleta Giratoria") # Titulo de la ventana

    # Cargar imágenes
    ruta_fondo = "assets/fondo.jpg"
    ruta_ruleta = "assets/ruleta.png"
    flecha_2 = pygame.image.load("assets/r1.png")

    imagen_fondo = pygame.image.load(ruta_fondo) # Cargar imagen de fondo
    imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (ALTO, ANCHO)) # Escalar imagen de fondo
    imagen_ruleta = pygame.image.load(ruta_ruleta) # Cargar imagen de la ruleta
    imagen_ruleta_escalada = pygame.transform.scale(imagen_ruleta, (550, 550)) # Escalar imagen de la ruleta
    flecha_img = pygame.transform.scale(flecha_2, (200, 200)) # Escalar imagen de la flecha

    # Datos de la ruleta
    ruleta_rect = imagen_ruleta_escalada.get_rect(center=(ALTO // 2, ANCHO // 2)) # Rectangulo de la ruleta
    angulo = 0 # Angulo de rotacion
    velocidad = 0 # Velocidad de rotacion
    seleccionar_angulo = 0 # Angulo final
    ralentizar = False # Bandera para ralentizar la ruleta
    tema_mostrado = False  # Bandera para mostrar el tema solo una vez
    fps = 60 # Velocidad de fotogramas por segundo
    clock = pygame.time.Clock()

    # Definir temaes y TEMAS
    TEMAS = ["Preguntas de Autos", "Preguntas de Juegos", "Preguntas de Television", "Preguntas Cargadas", "Preguntas de Autos", "Preguntas de Juegos", "Preguntas de Television", "Preguntas Cargadas"]
    NUM_TEMAS = len(TEMAS)
    sector_angulo = 360 // NUM_TEMAS  # Ángulo por sector (45° por sector)

    # Funcion para iniciar el giro
    def girar_ruleta():
        nonlocal velocidad, seleccionar_angulo, ralentizar, tema_mostrado # Variables no locales
        velocidad = random.randint(20, 30)  # Velocidad inicial aleatoria
        seleccionar_angulo = random.randint(0, 359)  # Ángulo final aleatorio
        ralentizar = False # Reiniciar la bandera para la nueva rotación
        tema_mostrado = False  # Reiniciar la bandera para el nuevo giro
        bandera_girada = True # Activar la bandera para mostrar el tema

        return bandera_girada

    # Funcion para determinar el tema
    def obtener_tema(angulo):
        # Convertir el ángulo en un sector
        angulo_ajustado = angulo % 360  # Asegurar que esta entre 0 y 359
        seleccionar_indice = int(angulo_ajustado // sector_angulo) # Determinar el sector
        return TEMAS[seleccionar_indice] # Devolver el tema correspondiente

    # Iniciar el primer giro
    fondo = pantalla.blit(imagen_fondo_escalar, (0, 0)) # Dibujar el fondo
    # Bucle principal
    girar = True # Bandera para el bucle principal
    while girar: 
        for event in pygame.event.get(): # Eventos del juego
            if event.type == pygame.QUIT: # Salir del juego
                girar = False # Salir del bucle principal
            if event.type == pygame.MOUSEBUTTONDOWN: # Hacer clic en la ruleta
                if ruleta_rect.collidepoint(event.pos): # Colision con la ruleta
                    bandera_girada = girar_ruleta() # Girar la ruleta

        # Dibujar el fondo
        pantalla.blit(imagen_fondo_escalar, (0, 0)) # Dibujar el fondo

        # Actualizar rotacion
        if velocidad > 0: # Girar la ruleta
            angulo += velocidad # Incrementar el ángulo
            angulo %= 360 # Asegurar que esta entre 0 y 359
            if ralentizar: # Ralentizar la ruleta
                velocidad -= 0.1 # Reducir la velocidad
        else:
            # Detener la ruleta y mostrar el tema una vez
            if bandera_girada:
                ralentizar = False # Reiniciar la bandera de ralentización
                tema_final = obtener_tema(angulo) # Obtener el tema
                tema_mostrado = True # Mostrar el tema
                girar = False # Evita mostrar el tema más de una vez

        # Inicia desaceleracion si está cerca del objetivo
        if not ralentizar and abs(angulo - seleccionar_angulo) <= 50: # Ralentizar la ruleta
            ralentizar = True # Ralentizar la ruleta
 
        # Rotar la ruleta
        
        rotar_imagen = pygame.transform.rotate(imagen_ruleta_escalada, angulo) # Rotar la ruleta
        rotal_rectangulo = rotar_imagen.get_rect(center=ruleta_rect.center) # Rectangulo de la ruleta rotada

        # Dibujar la ruleta
        pantalla.blit(rotar_imagen, rotal_rectangulo.topleft) # Dibujar la ruleta

      
        # Dibujar la flecha
        rotar_flecha = flecha_img.get_rect(center=ruleta_rect.center) # Rectangulo de la flecha
        pantalla.blit(flecha_img, rotar_flecha.topleft) # Dibujar la flecha

        # Actualizar la pantalla
        pygame.display.flip() # Actualizar la pantalla
        clock.tick(fps) # Controlar la velocidad de fotogramas
        

    return fondo, tema_final
