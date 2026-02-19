import arcade
from math import sin
from lab02_draw import dibujar_coche
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)


        self.coordsX = 50
    
    def on_draw(self):

        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.BLACK_OLIVE)
        dibujar_coche(sin(self.coordsX)*300,250)
        self.coordsX+=0.01

        # Poner aquí el código del dibujo
        # Cambiar la posición y/o tamaño del dibujo para crear animación
        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
