import pygame  # Importa la libreria Pygame para crear el juego.
import csv

ANCHO = 800
ALTO = 600
punto = 1
vida = 3
def abrir_cfg(csv):
    with open(csv, mode='r', encoding='utf-8') as archivo:
        lista = []
        csv_linea =  archivo.readlines()
        for linea in csv_linea:
            print(linea)
    #for i range linea:
    #    vida =
    #    tiempo =
    #    puntos =

abrir_cfg('config.csv')
        

#hacer archivo config, y leerlo, luego hacer una pantalla para poder congiurar la vida tiempo etc, 
CUADRO_ALTO = 40
CUADRO_ANCHO = 400  

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


    
    
