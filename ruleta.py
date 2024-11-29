import pygame
import sys
import random
from funciones import *

def jugar_ruleta():
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
                print(f"¡La ruleta se detuvo en el tema: {tema_final}!")
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




# 

# def dibujar_texto_con_boton_transparente(pantalla:surface, texto, x:int, y:int, ancho:int, alto:int, color_normal:tuple, color_hover:tuple, pos_mouse):
#     ''' 
#     ¿Para qué sirve?
#     Dibuja un botón con texto que cambia de color cuando el mouse pasa por encima (hover).

#     ¿Qué parámetro acepta?
#     - pantalla: (pygame.Surface) La superficie donde se dibuja el botón.
#     - texto: (str) El texto que se mostrará en el botón.
#     - x: (int) La posición en el eje X de la esquina superior izquierda del botón.
#     - y: (int) La posición en el eje Y de la esquina superior izquierda del botón.
#     - ancho: (int) El ancho del botón.
#     - alto: (int) El alto del botón.
#     - color_normal: (tuple) El color del texto cuando no hay hover.
#     - color_hover: (tuple) El color del texto cuando el mouse está encima del botón.
#     - pos_mouse: (tuple) Las coordenadas actuales del mouse.

#     ¿Qué retorna?
#     - pygame.Surface: El texto renderizado, que actúa como el "botón" visual.
#     '''
#     pos_mouse = pygame.mouse.get_pos()  # Obtiene la posición del mouse
#     color_texto = color_hover if x <= pos_mouse[0] <= x + ancho and y <= pos_mouse[1] <= y + alto else color_normal  # Cambia el color si el mouse está sobre el botón
#     fuente = pygame.font.SysFont("Showcard Gothic", 30)  # Selecciona la fuente
#     texto_renderizado = fuente.render(str(texto), True, color_texto)  # Renderiza el texto con el color adecuado
#     texto_rect = texto_renderizado.get_rect(center=(x + ancho // 2, y + alto // 2))  # Ajusta el rectángulo para centrar el texto en el botón
#     mostrar_texto = pantalla.blit(texto_renderizado, texto_rect)  # Dibuja el texto en la pantalla

#     return mostrar_texto  # Retorna la superficie con el texto renderizado



# #boton_jugar = dibujar_texto_con_boton_transparente (pantalla, "Jugar", 625,560, 100, 20 , CYAN1, CYAN1 , pos_mouse)