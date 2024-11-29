import csv
import os
from pathlib import Path
import random

# Función para elegir el tema de las preguntas
def elegir_tema(tema_final):
    '''
    ¿Para qué sirve?
    Esta función elige un tema de preguntas para cargar en el programa.
    
    ¿Qué parámetro acepta?
    - tema_final: (str) El tema elegido por el usuario. Es una cadena que especifica el tema deseado (por ejemplo, "Preguntas de Autos").
    
    ¿Qué retorna?
    - path_csv: (Path) La ruta al archivo CSV con las preguntas del tema elegido. Se devuelve la ruta donde están almacenadas las preguntas del tema.
    '''
    # Comprobamos el tema elegido y asignamos el archivo correspondiente
    if tema_final == "Preguntas de Autos":
        path_csv = Path('preguntas_autos.csv')  # Ruta al archivo CSV de preguntas de autos
    elif tema_final == "Preguntas de Juegos":
        path_csv = Path('preguntas_juegos.csv')  # Ruta al archivo CSV de preguntas de juegos
    elif tema_final == "Preguntas de Television":
        path_csv = Path('preguntas_tv.csv')  # Ruta al archivo CSV de preguntas de televisión
    elif tema_final == "Preguntas Cargadas":
        path_csv = Path('preguntas_cargadas.csv')  # Ruta al archivo CSV de preguntas cargadas previamente
        
    return path_csv  # Retorna la ruta al archivo correspondiente

# Función para cargar las preguntas desde un archivo CSV
def cargar_preguntas_desde_csv(archivo_csv):
    '''
    ¿Para qué sirve?
    Esta función carga las preguntas desde un archivo CSV y las organiza en una lista de listas con pregunta, respuestas y respuesta correcta.
    
    ¿Qué parámetro acepta?
    - archivo_csv: (Path) El archivo CSV desde donde se cargan las preguntas. Es la ruta del archivo CSV que contiene las preguntas y respuestas.
    
    ¿Qué retorna?
    - preguntas: (list) Lista con las preguntas, respuestas y la respuesta correcta. Cada pregunta es una lista con la estructura [pregunta, respuesta1, respuesta2, respuesta3, respuesta_correcta].
    '''
    preguntas = []  # Lista vacía para almacenar las preguntas
    # Abrimos el archivo CSV en modo lectura
    with open(archivo_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)  # lector de CSV
        next(lector)  # Saltamos la primera línea del archivo, que contiene los encabezados
        # Iteramos sobre las filas del archivo
        for fila in lector:
            pregunta = fila[0]  # La primera columna es la pregunta
            respuestas = fila[1:4]  # Las siguientes tres columnas son las respuestas
            respuesta_correcta = fila[4]  # La última columna es la respuesta correcta
            # Almacenamos la pregunta y sus respuestas como una lista
            preguntas.append([pregunta] + respuestas + [respuesta_correcta])  
    return preguntas  # Retorna la lista de preguntas con sus respuestas

# Función para mezclar las respuestas de una pregunta
def mezclar_respuestas(lista_respuestas):
    ''' 
    ¿Para qué sirve?
    Esta función mezcla las respuestas de una pregunta para que no siempre estén en el mismo orden.
    
    ¿Qué parámetro acepta?
    - respuestas: (list) Lista de respuestas a una pregunta. Es una lista con las opciones de respuestas para una pregunta.
    
    ¿Qué retorna?
    - respuestas_mezcladas: (list) Lista de respuestas mezcladas. Devuelve una nueva lista donde las respuestas están en un orden aleatorio.
    '''
    respuestas_mezcladas = lista_respuestas.copy()  # Hacemos una copia de la lista de respuestas
    random.shuffle(respuestas_mezcladas)  # Mezclamos las respuestas usando random.shuffle
    return respuestas_mezcladas  # Retorna la lista de respuestas mezcladas
