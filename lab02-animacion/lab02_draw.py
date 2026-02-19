
import arcade

def dibujar_coche (x,y,color):
    arcade.draw_rect_filled(arcade.XYWH(x, y+67, 140, 80), color)
    arcade.draw_rect_filled(arcade.XYWH(x, y, 300, 80), color)
    arcade.draw_circle_filled(x-60,y-43,40, arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_circle_filled(x+60,y-43,40, arcade.color.BLACK_LEATHER_JACKET)

