# main.py ARCHIVO PRINCIPAL
#ESTE ARCHIVO INICIA EL JUEGO Y LO MANTIENE EN EJECUCION.

from scripts.juego import Juego #importa la clase juego desde juego.py

#Si ejecutamos este archivo directamente, se ejecuta el juego
if __name__ == "__main__": #Verifica que el script se ejecuta directamente
    juego = Juego() #Crea una instancia del juego
    juego.ejecutar() #Llama al metodo que ejecuta el bucle principal del juego
    juego.salir() #Llama al metodo para cerrar Pygame correctamente.
