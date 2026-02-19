
import arcade
arcade.open_window(500, 500, "Drawing Example")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.BITTER_LIME)

def dibujar_coche (x,y,escala):
    arcade.draw_rect_filled(arcade.XYWH(250, 250, 140, 80), arcade.color.MSU_GREEN)
    arcade.draw_rect_filled(arcade.XYWH(250, 183, 300, 80), arcade.color.MSU_GREEN)
    arcade.draw_circle_filled(190,140,40, arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_circle_filled(310,140,40, arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_parabola_filled(120,150,80,40,(255, 165, 0),90)

arcade.finish_render()
arcade.run()