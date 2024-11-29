import pygame
from funciones import *
from colores import *
from configuraciones import *

# Función para mostrar una animación o "easter egg" con imágenes de gatos
def easter_egg(pantalla, pos_mouse):
    ''' 
    Muestra un "Easter Egg" en forma de imágenes de gatos en la pantalla y un botón para volver al menú.
    '''
    # Establecer el título de la ventana
    pygame.display.set_caption("Easter egg?? o.o")

    # Cargar las imágenes de los gatos para el Easter egg
    ruta_gato_1 = 'assets/gato_easter_egg.jpg'
    imagen_gato_1 = pygame.image.load(ruta_gato_1)
    
    ruta_gato_2 = 'assets/gato_egg.jpg'
    imagen_gato_2 = pygame.image.load(ruta_gato_2)
    
    ruta_gatito = 'assets/gatito.jpg'
    imagen_gatito = pygame.image.load(ruta_gatito)

    # Dibujar las imágenes en la pantalla en diferentes posiciones
    pantalla.blit(imagen_gato_1, (0, 0))  # Gato grande en la parte superior izquierda
    pantalla.blit(imagen_gato_2, (0, 400))  # Gato 2 en la parte inferior izquierda
    pantalla.blit(imagen_gatito, (600, 0))  # Gatito pequeño en la parte superior derecha

    # Obtener la posición del mouse para manejar la interacción con el botón
    pos_mouse = pygame.mouse.get_pos()  # Obtiene la posición actual del mouse

    # Dibujar el botón "Volver al Menu" con detección de hover (cambio de color al pasar el mouse)
    boton_volver_menu = dibujar_texto_con_boton_transparente(
        pantalla, 
        "Volver al Menu", 
        620, 550, 200, 50,  # Posición y tamaño del botón
        WHEAT1, RED1,  # Colores para el estado normal y hover
        pos_mouse  # Posición del mouse para detección de hover
    )

    # Actualizar la pantalla para reflejar los cambios
    pygame.display.flip()

    # Retornar el botón de "Volver al Menu" para manejar la interacción
    return boton_volver_menu
