import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Set the background color
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)


    def on_draw(self):
        arcade.start_render()
        pine_tree(100, 100)  # Adjust position as needed
        pine_tree(200, 200)  # Adjust position as needed




def pine_tree(x, y):
    arcade.draw_xywh_rectangle_filled(x + 420, y + 200, 20, 71, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(x + 390, y + 220, x + 470, y + 220, x + 430, y + 240, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(x + 395, y + 230, x +465, y + 230, x + 430, y + 255, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(x +400, y + 240, x + 460, y + 240, x + 430, y + 270, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(x +405, y + 240, x + 455,  y + 240, x + 430, y + 285, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(x +410, y + 240, x + 450, y + 240, x + 430, y + 300, arcade.csscolor.LIGHT_GREEN)


def main():
    window = MyGame()

    arcade.run()



main()
