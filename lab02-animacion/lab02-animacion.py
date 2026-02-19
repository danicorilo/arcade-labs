import arcade
from math import sin, tan, tanh, sinh, log, e, pi, cos
from lab02_draw import dibujar_coche
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)


        self.coordsX = 50
        self.coordsX2= 40
        self.coordsX3=pi
    
    def on_draw(self):

        self.clear()
        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.BLACK_OLIVE)
        dibujar_coche((tan(self.coordsX))*200,250, arcade.color.AFRICAN_VIOLET)
        dibujar_coche(tan(self.coordsX)*500, 190, arcade.color.ALABAMA_CRIMSON)
        dibujar_coche((tan((self.coordsX))*sin(self.coordsX))*500,130, arcade.color.YELLOW)
        dibujar_coche(tan(self.coordsX3)*20,100,arcade.color.ALMOND)
        self.coordsX+=0.01
        self.coordsX2+=2
        self.coordsX3+=0.012
        

        # Poner aquí el código del dibujo
        # Cambiar la posición y/o tamaño del dibujo para crear animación
        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
