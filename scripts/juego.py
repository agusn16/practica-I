# juego.py - Logica principal del juego
#AQUI DEFINIMOS LA CLASE "juego", que maneja la ventana, los eventos y la actualizaion del juego.


import pygame #importamos PYgame
from scripts.jugador import Jugador #importamos la clase jugador

# Configuración inicial
ANCHO, ALTO = 800, 600 #Tamaño de la ventanadel juego
FPS = 60 #cuantos duadros pos segundos queremos que corra el juego

class Juego:
    def __init__(self):
        pygame.init() #Inicializamos Pygame
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))#Creamos la ventana del juego
        pygame.display.set_caption("Juego de Supervivencia")#Titulo de la ventana
        self.reloj = pygame.time.Clock()#Reloj para controlar FPS
        self.jugando = True #Variable que controla si el juego sigue activo

        # Crear jugador con los límites de la pantalla
        self.jugador = Jugador(ANCHO // 2, ALTO // 2, ANCHO, ALTO)

    def ejecutar(self):
        """Bucle principal del juego"""
        while self.jugando:
            self.reloj.tick(FPS)#Mantiene el juego en 60 FPS
            self.manejar_eventos()#Maneja los eventos del teclado y el raton
            self.actualizar()#actualiza la logica del juego
            self.dibujar()#Dibuja los elementos en la pantalla

    def manejar_eventos(self):
        """Detecta eventos como cerrar el juego o presionar teclas"""
        for evento in pygame.event.get():#Recorremos todos los eventos
            if evento.type == pygame.QUIT:#si el usuario cierra la ventana
                self.jugando = False#Terminamos el bucle del juego

    def actualizar(self):
        """Actualiza los elementos del juego (movimiento del jugador, logica, etc.)"""
        teclas = pygame.key.get_pressed()#Detectamos que teclas estan presionandas
        self.jugador.mover(teclas)#Movemos el jugador con esas teclas

    def dibujar(self):
        """Dibujar los elementos en la pantalla"""
        self.pantalla.fill((0, 150, 0))  # Fondo verde
        self.jugador.dibujar(self.pantalla)#Dibujamos el jugador en la pantalla
        pygame.display.flip()#Actualizamos la pantalla con los nuevos graficos

    def salir(self):
        """cierra Pygame correctamente"""
        pygame.quit()

#Si ejecutamos este archivo directamente, se ejecuta el juego
if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
    juego.salir()



