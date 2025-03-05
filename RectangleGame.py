import pygame

# Inicializar pygame
pygame.init()

# Definir constantes
ANCHO, ALTO = 600, 600  # Tamaño de la ventana
FILAS, COLUMNAS = 10, 10  # Grid de 10x10
TAM_CELDA = ANCHO // COLUMNAS  # Tamaño de cada celda

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Movimiento en Grid")

# Definir personaje (posición en la grid)
personaje_x, personaje_y = 0, 0  # Posición en términos de celdas
color_personaje = (0, 255, 0)  # Verde

# Bucle principal
ejecutando = True
while ejecutando:
    pygame.time.delay(100)  # Control de la velocidad del juego

    # Capturar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Capturar teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and personaje_x > 0:
        personaje_x -= 1  # Mover una celda a la izquierda
    if teclas[pygame.K_RIGHT] and personaje_x < COLUMNAS - 1:
        personaje_x += 1  # Mover una celda a la derecha
    if teclas[pygame.K_UP] and personaje_y > 0:
        personaje_y -= 1  # Mover una celda arriba
    if teclas[pygame.K_DOWN] and personaje_y < FILAS - 1:
        personaje_y += 1  # Mover una celda abajo

    # Dibujar fondo y cuadrícula
    pantalla.fill((0, 0, 0))  # Fondo negro
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            pygame.draw.rect(pantalla, (50, 50, 50), (col * TAM_CELDA, fila * TAM_CELDA, TAM_CELDA, TAM_CELDA), 1)

    # Dibujar personaje
    pygame.draw.rect(
        pantalla,
        color_personaje,
        (personaje_x * TAM_CELDA, personaje_y * TAM_CELDA, TAM_CELDA, TAM_CELDA)
    )

    # Actualizar pantalla
    pygame.display.update()

# Cerrar pygame
pygame.quit()

