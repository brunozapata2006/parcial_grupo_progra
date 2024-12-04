import pygame

def inicializar_tiempo(evento_timer, intervalo=1000):
    '''
    Plantilla Documentacion
    ¿Para que sirve? Inicializa un evento de temporizador que se ejecuta cada intervalo.
    ¿Que parametro acepta?
    - evento_timer: El identificador del evento.
    - intervalo: Tiempo en milisegundos entre cada evento (por defecto, 1000 ms = 1 segundo).
    ¿Que Retorna?
    No retorna ningún valor.
    '''
    pygame.time.set_timer(evento_timer, intervalo)

def actualizar_tiempo_restante(tiempo_restante):
    '''
    Plantilla Documentacion
    ¿Para que sirve? Actualiza el tiempo restante disminuyéndolo en un segundo.
    ¿Que parametro acepta?
    - tiempo_restante: Tiempo restante en segundos.
    ¿Que Retorna?
    - tuple: Tiempo restante actualizado y una bandera indicando si el tiempo se agotó.
    '''
    tiempo_restante -= 1
    tiempo_agotado = tiempo_restante <= 0
    return max(tiempo_restante, 0), tiempo_agotado

def mostrar_tiempo_restante(pantalla, tiempo_restante, fuente, color):
    '''
    Plantilla Documentacion
    ¿Para que sirve? Muestra el tiempo restante en la pantalla del juego.
    ¿Que parametro acepta?
    - pantalla: La superficie donde se dibuja el texto.
    - tiempo_restante: El tiempo restante a mostrar en segundos.
    - fuente: Fuente para renderizar el texto.
    - color: Color del texto en formato RGB.
    ¿Que Retorna?
    No retorna ningún valor.
    '''
    # Renderiza el texto del tiempo
    texto_tiempo = fuente.render(f"{tiempo_restante}", True, color)
    # Obtén el rectángulo del texto y ajusta la posición
    texto_rect = texto_tiempo.get_rect(center=(400, 50))  # Centro horizontal, posición Y=50
    # Dibuja el texto en la pantalla
    pantalla.blit(texto_tiempo, texto_rect)

def manejar_tiempo_agotado(pregunta_actual_index, vidas, max_preguntas):
    '''
    Plantilla Documentacion
    ¿Para que sirve? Maneja la lógica cuando el tiempo se agota, pasando a la siguiente pregunta y restando una vida.
    ¿Que parametro acepta?
    - pregunta_actual_index: Índice actual de la pregunta.
    - vidas: Número de vidas restantes.
    - max_preguntas: Número máximo de preguntas disponibles.
    ¿Que Retorna?
    - tuple: Índice de la siguiente pregunta y el número actualizado de vidas.
    '''
    vidas -= 1
    pregunta_actual_index += 1
    if pregunta_actual_index >= max_preguntas:
        pregunta_actual_index = max_preguntas  # Evitar exceder el límite.
    return pregunta_actual_index, vidas
