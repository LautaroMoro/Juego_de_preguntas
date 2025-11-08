import sys, os
import pygame

RUTA_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if RUTA_RAIZ not in sys.path:
    sys.path.insert(0, RUTA_RAIZ)

from base_datos import crear_tablas
from PantallaPrincipal import pantalla_principal_juego
def main():
    crear_tablas()
    pygame.init()
    pygame.mixer.init()
    pantalla_principal_juego()
    pygame.quit()
if __name__ == "__main__":
    main()