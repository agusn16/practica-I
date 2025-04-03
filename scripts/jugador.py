#jugador.py - Clase del jugador
#AQUI CREAMOS LA CLASE "jugador",QUE MANEJA EL PERSONAJE EN PANTALLA

import pygame

class Jugador:
    def __init__(self, x, y, ancho_pantalla, alto_pantalla):
        self.image = pygame.Surface((40, 40))  # Cuadrado de 40x40
        self.image.fill((255, 255, 0))  # Color amarillo
        self.rect = self.image.get_rect(topleft=(x, y))#Lo posiciona en x, y
        self.velocidad = 5 #Velocidad de movimiento
        self.ancho_pantalla = ancho_pantalla #Ancho de la pantalla
        self.alto_pantalla = alto_pantalla #Alto de la pantalla

    def mover(self, teclas):
        """Mueve al jugador con restricciones de borde"""
        if teclas[pygame.K_LEFT] and self.rect.left > 0: 
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < self.ancho_pantalla:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN] and self.rect.bottom < self.alto_pantalla:
            self.rect.y += self.velocidad

    def dibujar(self, pantalla):
        """Dibuja al jugador en la pantalla"""
        pantalla.blit(self.image, self.rect)
