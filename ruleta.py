import pygame
import sys
import random
from funciones import *

def jugar_ruleta():
    '''
    Plantilla Documentacion
    ¿Para qué sirve?
    Esta función gestiona un juego de ruleta giratoria en Pygame. El jugador puede hacer clic en la ruleta para hacerla girar, y luego se detiene mostrando un tema aleatorio basado en la posición de la ruleta.

    ¿Qué parámetro acepta?
    - Ninguno.

    ¿Qué retorna?
    - fondo: (Surface) La superficie del fondo renderizada.
    - tema_final: (str) El tema seleccionado aleatoriamente en base a la posición de la ruleta.
    '''
    bandera_girada = False
    # Configuración inicial
    pygame.init()
    ALTO, ANCHO = 800, 600
    pantalla = pygame.display.set_mode((ALTO, ANCHO), pygame.RESIZABLE)
    pygame.display.set_caption("Ruleta Giratoria")

    # Cargar imágenes
    ruta_fondo = "assets/fondo.jpg"
    ruta_ruleta = "assets/ruleta.png"
    flecha_2 = pygame.image.load("assets/r1.png")

    imagen_fondo = pygame.image.load(ruta_fondo)
    imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (ALTO, ANCHO))
    imagen_ruleta = pygame.image.load(ruta_ruleta)
    imagen_ruleta_escalada = pygame.transform.scale(imagen_ruleta, (550, 550))
    flecha_img = pygame.transform.scale(flecha_2, (200, 200))

    # Datos de la ruleta
    ruleta_rect = imagen_ruleta_escalada.get_rect(center=(ALTO // 2, ANCHO // 2))
    angulo = 0
    velocidad = 0
    seleccionar_angulo = 0
    ralentizar = False
    tema_mostrado = False  # Bandera para mostrar el tema solo una vez
    fps = 60
    clock = pygame.time.Clock()

    # Definir temaes y TEMAS
    TEMAS = ["Preguntas de Autos", "Preguntas de Juegos", "Preguntas de Television", "Preguntas Cargadas", "Preguntas de Autos", "Preguntas de Juegos", "Preguntas de Television", "Preguntas Cargadas"]
    NUM_TEMAS = len(TEMAS)
    sector_angulo = 360 // NUM_TEMAS  # Ángulo por sector (45° por sector)

    # Función para iniciar el giro
    def girar_ruleta():
        nonlocal velocidad, seleccionar_angulo, ralentizar, tema_mostrado
        velocidad = random.randint(20, 30)  # Velocidad inicial aleatoria
        seleccionar_angulo = random.randint(0, 359)  # Ángulo final aleatorio
        ralentizar = False
        tema_mostrado = False  # Reiniciar la bandera para el nuevo giro
        bandera_girada = True

        return bandera_girada

    # Función para determinar el tema
    def obtener_tema(angulo):
        # Convertir el ángulo en un sector
        angulo_ajustado = angulo % 360  # Asegurar que esté entre 0 y 359
        seleccionar_indice = int(angulo_ajustado // sector_angulo)
        return TEMAS[seleccionar_indice]

    # Iniciar el primer giro
    #girar_ruleta()
    fondo = pantalla.blit(imagen_fondo_escalar, (0, 0))
    # Bucle principal
    girar = True
    while girar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                girar = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ruleta_rect.collidepoint(event.pos):
                    bandera_girada = girar_ruleta()

        # Dibujar el fondo
        pantalla.blit(imagen_fondo_escalar, (0, 0))

        # Actualizar rotación
        if velocidad > 0:
            angulo += velocidad
            angulo %= 360
            if ralentizar:
                velocidad -= 0.1
        else:
            # Detener la ruleta y mostrar el tema una vez
            if bandera_girada:
                ralentizar = False
                tema_final = obtener_tema(angulo)
                tema_mostrado = True
                girar = False # Evita mostrar el tema más de una vez

        # Inicia desaceleración si está cerca del objetivo
        if not ralentizar and abs(angulo - seleccionar_angulo) <= 50:
            ralentizar = True

        # Rotar la ruleta
        #fondo = pantalla.blit(imagen_fondo_escalar, (0, 0)) ###################
        rotar_imagen = pygame.transform.rotate(imagen_ruleta_escalada, angulo)
        rotal_rectangulo = rotar_imagen.get_rect(center=ruleta_rect.center)

        # Dibujar la ruleta
        pantalla.blit(rotar_imagen, rotal_rectangulo.topleft)

        # Dibujar la flecha fija
        # rotar_flecha = flecha_2.get_rect(center=ruleta_rect.center)
        # pantalla.blit(flecha_2, rotar_flecha.topleft)

        rotar_flecha = flecha_img.get_rect(center=ruleta_rect.center)
        pantalla.blit(flecha_img, rotar_flecha.topleft)

        # Actualizar la pantalla
        pygame.display.flip()
        clock.tick(fps)
        # fondo = pantalla.blit(imagen_fondo_escalar, (0, 0))

    return fondo, tema_final
