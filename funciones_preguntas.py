import csv
import os
from pathlib import Path
import random


def elegir_tema(tema_final):
    '''
¿Para qué sirve?
Esta función elige un tema de preguntas para cargar en el programa.
¿Qué parámetro acepta?
- tema_final: (str) El tema elegido por el usuario.
¿Qué retorna?
- path_csv: (Path) La ruta al archivo CSV con las preguntas del tema elegido.
'''
    print (tema_final)
    if tema_final == "Preguntas de Autos":
        path_csv = Path('parcial_grupo/preguntas_autos.csv')
    elif tema_final == "Preguntas de Juegos":
        path_csv = Path('preguntas_juegos.csv')
    elif tema_final == "Preguntas de Television":
        path_csv = Path('preguntas_tv.csv')
    elif tema_final == "Preguntas Cargadas":
        path_csv = Path('preguntas_cargadas.csv')
        
    return path_csv

def cargar_preguntas(path_csv):
    ''' 
    ¿Para qué sirve?
    Esta función carga las preguntas de un archivo CSV y las devuelve en una lista.

    ¿Qué parámetro acepta?
    - path_csv: (Path) Ruta al archivo CSV donde se encuentran las preguntas.

    ¿Qué retorna?
    - preguntas: (list) Lista de listas, donde cada sublista contiene una pregunta y sus respuestas.
    '''

    datos = []  # Lista para almacenar las preguntas y respuestas como pares
    with open(path_csv, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Omitir encabezado
        for fila in lector:
            pregunta = [fila[0]]  # La pregunta como una lista
            respuestas = fila[1:]  # Las respuestas como una lista
            datos.append(pregunta + respuestas)  # Combina pregunta y respuestas en una sola lista
        print (datos)
    return datos


#probar funciones
# path_csv = elegir_tema("Autos")
# preguntas = cargar_preguntas(path_csv)
#print(preguntas)


def mezclar_respuestas(lista_respuestas):
    ''' 
    ¿Para qué sirve?
    Esta función mezcla las respuestas de una pregunta para que no siempre estén en el mismo orden.

    ¿Qué parámetro acepta?
    - respuestas: (list) Lista de respuestas a una pregunta.

    ¿Qué retorna?
    - respuestas_mezcladas: (list) Lista de respuestas mezcladas.
    '''
  
    respuestas_mezcladas = lista_respuestas.copy()  # Copia la lista de respuestas
    random.shuffle(respuestas_mezcladas)  # Mezcla las respuestas
    return respuestas_mezcladas