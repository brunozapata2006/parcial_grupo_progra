from colores import *  # Importa los colores definidos en otro archivo
import pygame  # Libreria principal para crear juegos en 2D
from pathlib import Path  # Para trabajar con rutas de archivos
from configuraciones import *  # Importa configuraciones (posiblemente con mas valores de colores, configuraciones de juego, etc.)
from pygame import surface  # Importa la clase 'surface' de pygame para trabajar con superficies (pantallas)

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
    

# Funcion para guardar los textos introducidos en un archivo CSV
def guardar_textos(textos_guardados, path_csv):
    '''
    Plantilla Documentacion
    
    ¿Para qua sirve? 
    Esta funcion guarda los textos introducidos en una lista en un archivo CSV. Los textos se guardan solo si todos los cuadros contienen contenido (ningun cuadro vacio).

    ¿Qua parametros acepta?
    - textos_guardados: (list) Lista que contiene los textos que se guardaran en el archivo CSV. Debe contener una pregunta y cuatro respuestas.
    - path_csv: (Path) Ruta del archivo CSV donde se guardaran los textos.

    ¿Qua retorna?
    - None. La funcion guarda los textos en el archivo CSV si todos los cuadros tienen contenido y no retorna ningun valor.
    '''
    todos_contenido = True  # Se inicializa una variable para verificar si todos los cuadros tienen contenido
    for texto in textos_guardados:  # Recorre cada texto en la lista
        if texto == "":  # Si algun texto esta vacio, marca como False
            todos_contenido = False
            break  # Sale del bucle si encuentra un cuadro vacio

    if todos_contenido:  # Si todos los cuadros tienen texto
        archivo_existe = path_csv.exists()  # Verifica si el archivo ya existe

        with open(path_csv, 'a', newline='', encoding='utf-8') as archivo:  # Abre el archivo en modo de append
            if not archivo_existe:  # Si el archivo no existe, escribe la cabecera
                archivo.write("Pregunta,Respuesta 1,Respuesta 2,Respuesta 3,Respuesta correcta\n")

            archivo.write(",".join(textos_guardados) + "\n")  # Guarda los textos como una nueva fila en el archivo CSV


# Funcion para gestionar los eventos de entrada de texto (por ejemplo, teclas presionadas)
def gestionar_eventos_entrada(evento, cuadro_activo, cuadros_texto):
    ''' 
    ¿Para quo sirve?
    Esta funcion gestiona los eventos de teclado para escribir en los cuadros de texto o cambiar de cuadro.

    ¿Qua parametro acepta?
    - evento: (pygame.event.Event) El evento generado por las teclas del teclado (escribir por ejemplo)
    - cuadro_activo: (int) El indice del cuadro de texto actualmente activo (de 0 a 4, siendo 0 la pregunta)
    - cuadros_texto: (list) Lista de cadenas que representan el texto en cada cuadro.

    ¿Qua retorna?
    - cuadro_activo: (int) El indice actualizado del cuadro de texto activo.
    - cuadros_texto: (list) La lista actualizada con el texto introducido.
    '''
    path_csv = Path('preguntas_cargadas.csv')  # Ruta al archivo CSV donde se guardaran los textos
    
    if evento.type == pygame.KEYDOWN:  # Si se presiona una tecla
        if cuadro_activo < 5:  # Si el cuadro activo esta dentro del rango valido
            if evento.key == pygame.K_BACKSPACE:  # Si se presiona la tecla BACKSPACE
                cuadros_texto[cuadro_activo] = cuadros_texto[cuadro_activo][:-1]  # Elimina el ultimo caracter
            elif evento.key == pygame.K_RETURN:  # Si se presiona la tecla ENTER
                if cuadro_activo < 4:  # Si no estamos en el ultimo cuadro
                    cuadro_activo += 1  # Cambia al siguiente cuadro de texto
                else:  # Si es el ultimo cuadro, guarda y limpia
                    guardar_textos(cuadros_texto, path_csv)  # Guarda los textos en el CSV
                    cuadros_texto = ["", "", "", "", ""]  # Limpia los cuadros de texto
                    cuadro_activo = 0  # Reinicia el cuadro activo a 0
            else: 
                if len(cuadros_texto[cuadro_activo]) < 50:  # Añadir un limite de caracteres por cuadro
                    cuadros_texto[cuadro_activo] += evento.unicode  # Añade el caracter al cuadro activo

    return cuadro_activo, cuadros_texto  # Devuelve el indice del cuadro activo y la lista de textos actualizada


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


# Funcion para limpiar la pantalla y mostrar un fondo
def limpiar_pantalla():
    '''
    ¿Para qua sirve?
    Esta funcion limpia la pantalla y dibuja un fondo.
    
    ¿Qua parametro acepta?
    - Ninguno.
    
    ¿Qua retorna?
    - None. La funcion solo limpia la pantalla y muestra un fondo.
    '''
    ruta_fondo = 'assets/fondo.jpg'  # Ruta de la imagen de fondo
    imagen_fondo = pygame.image.load(ruta_fondo)  # Carga la imagen de fondo
    imagen_fondo_escalar = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))  # Escala la imagen para ajustarla a la pantalla
    pygame.display.flip()  # Actualiza la pantalla
