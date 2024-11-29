import pygame
from funciones import *
from colores import *
from configuraciones import *

def easter_egg(pantalla, pos_mouse):  

    pygame.display.set_caption("Easter egg?? o.o")
    
    ruta_gato_1 = 'assets/gato_easter_egg.jpg'
    imagen_gato_1 = pygame.image.load(ruta_gato_1)
    ruta_gato_2 = 'assets/gato_egg.jpg'
    imagen_gato_2 = pygame.image.load(ruta_gato_2)
    ruta_gatito = 'assets/gatito.jpg'
    imagen_gatito = pygame.image.load(ruta_gatito)
    
    pantalla.blit(imagen_gato_1, (0, 0))
    pantalla.blit(imagen_gato_2, (0, 400))
    pantalla.blit(imagen_gatito, (600, 0))
    
    pos_mouse = pygame.mouse.get_pos                                                     #x   #y #ancho #alto
    boton_volver_menu = dibujar_texto_con_boton_transparente(pantalla, "Volver al Menu", 620, 550, 200, 50, WHEAT1, RED1, pos_mouse)
    
    pygame.display.flip()
    
    return boton_volver_menu