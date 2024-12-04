import pygame  # Importa la libreria Pygame para crear el juego.
import csv

ANCHO = 800 # Ancho de la ventana del juego.
ALTO = 600 # Alto de la ventana del juego.


def abrir_cfg(csv_path):
    '''
    ¿Para qué sirve?
    Abre un archivo CSV y lee los valores de vida, tiempo y punto.
    
    ¿Qué parámetros acepta?
    - csv_path: (str) La ruta del archivo CSV que se abrirá.
    
    ¿Qué retorna?
    - (int, int, int): Devuelve una tupla con los valores de vida, tiempo y punto leídos del archivo CSV.
    '''
    # Valores por defecto
    vida_defecto = 3
    tiempo_defecto = 5
    punto_defecto = 1

    with open(csv_path, mode='r', encoding='utf-8') as archivo:  # Modo lectura
        lector = csv.reader(archivo)  # Crear objeto lector
        next(lector)  # Saltar la cabecera
        for linea in lector:
            # Validar y asignar valores para cada campo
            if linea[0].strip():  # Si no está vacío o en blanco
                vida = int(linea[0])
            else:
                vida = vida_defecto

            if linea[1].strip():
                tiempo = int(linea[1])
            else:
                tiempo = tiempo_defecto

            if linea[2].strip():
                punto = int(linea[2])
            else:
                punto = punto_defecto
    
    return vida, tiempo, punto  # Devolver los valores de vida, tiempo y punto




# Procesamiento
vida, tiempo, punto = abrir_cfg("config.csv") # Leer los valores de vida, tiempo y punto
print(f"Vida: {vida}, Tiempo(en seg): {tiempo}, Puntos: {punto}") # Mostrar los valores leídos

# Configuración de la ventana
CUADRO_ALTO = 40 # Alto de los cuadros de texto
CUADRO_ANCHO = 400 # Ancho de los cuadros de texto

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


