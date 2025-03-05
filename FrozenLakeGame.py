import gymnasium as gym
import pygame
import numpy as np

# Inicializar pygame
pygame.init()

# Crear el entorno FrozenLake
env = gym.make("FrozenLake-v1", render_mode="rgb_array", is_slippery=False)
obs, info = env.reset()

# Obtener el tamaño de la imagen del entorno
render = env.render()
ALTO, ANCHO, _ = render.shape  # Obtener dimensiones
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Frozen Lake - Mueve con Flechas")

# Diccionario de teclas a acciones de FrozenLake
acciones = {
    pygame.K_LEFT: 2,  # Izquierda
    pygame.K_DOWN: 1,  # Abajo
    pygame.K_RIGHT: 0,  # Derecha
    pygame.K_UP: 3      # Arriba
}

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key in acciones:
                accion = acciones[evento.key]  # Obtener la acción de la tecla
                obs, reward, done, truncated, info = env.step(accion)

                # Dibujar la imagen del entorno en Pygame
                render = env.render()
                imagen = pygame.surfarray.make_surface(np.rot90(render, 1))  # Rotar para alinear con Pygame
                pantalla.blit(imagen, (0, 0))
                pygame.display.update()

                if done:
                    pygame.time.delay(1000)  # Esperar un segundo si termina
                    obs, info = env.reset()  # Reiniciar el juego

env.close()
pygame.quit()
