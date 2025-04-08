import arcade
from arcade.examples.array_backed_grid import SCREEN_WIDTH

#Constants
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

class Ships(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

        self.player_sprite = arcade.Sprite("ship (7).png", SPRITE_SCALING_PLAYER)

    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y

class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Ship Battle")

    def setup(self):
        self.score=0

    def draw_island01(self):
        tile_06 = arcade.Sprite("tile_06.png", 1.0)
        tile_06.center_x = 100
        tile_06.center_y = 900
        tile_06.draw()

        tile_07 = arcade.Sprite("tile_07.png", 1.0)
        tile_07.center_x = 160
        tile_07.center_y = 899
        tile_07.draw()

        tile_07 = arcade.Sprite("tile_07.png", 1.0)
        tile_07.center_x = 220
        tile_07.center_y = 899
        tile_07.draw()

        tile_09 = arcade.Sprite("tile_09.png",1.0)
        tile_09.center_x = 280
        tile_09.center_y = 899
        tile_09.draw()

        tile_25 = arcade.Sprite("tile_25.png", 1.0)
        tile_25.center_x = 280
        tile_25.center_y = 840
        tile_25.draw()

        tile_25 = arcade.Sprite("tile_25.png", 1.0)
        tile_25.center_x = 280
        tile_25.center_y = 800
        tile_25.draw()

        tile_57 = arcade.Sprite("tile_57.png", 1.0)
        tile_57.center_x = 280
        tile_57.center_y = 760
        tile_57.draw()


        tile_56 = arcade.Sprite("tile_56.png", 1.0)
        tile_56.center_x = 180
        tile_56.center_y = 760
        tile_56.draw()

        tile_82 = arcade.Sprite("tile_82.png", 1.0)
        tile_82.center_x = 220
        tile_82.center_y = 760
        tile_82.draw()

        tile_56 = arcade.Sprite("tile_56.png", 1.0)
        tile_56.center_x = 160
        tile_56.center_y = 760
        tile_56.draw()

        tile_54 = arcade.Sprite("tile_54.png", 1.0)
        tile_54.center_x = 100
        tile_54.center_y = 760
        tile_54.draw()

        tile_22 = arcade.Sprite("tile_22.png", 1.0)
        tile_22.center_x = 100
        tile_22.center_y = 820
        tile_22.draw()

        tile_22 = arcade.Sprite("tile_22.png", 1.0)
        tile_22.center_x = 100
        tile_22.center_y = 840
        tile_22.draw()

        tile_40 = arcade.Sprite("tile_40.png", 1.0)
        tile_40.center_x = 220
        tile_40.center_y = 820
        tile_40.draw()

        tile_39 = arcade.Sprite("tile_39.png",1.0)
        tile_39.center_x = 220
        tile_39.center_y = 840
        tile_39.draw()

        tile_23 = arcade.Sprite("tile_23.png", 1.0)
        tile_23.center_x = 160
        tile_23.center_y = 840
        tile_23.draw()

        tile_24 = arcade.Sprite("tile_24.png", 1.0)
        tile_24.center_x = 200
        tile_24.center_y = 840
        tile_24.draw()

        tile_23 = arcade.Sprite("tile_23.png", 1.0)
        tile_23.center_x = 160
        tile_23.center_y = 820
        tile_23.draw()

        tile_71 = arcade.Sprite("tile_71.png",1.0)
        tile_71.center_x = 150
        tile_71.center_y = 840
        tile_71.draw()

        tile_88 = arcade.Sprite("tile_88.png", 1.0)
        tile_88.center_x = 230
        tile_88.center_y = 820
        tile_88.draw()

        tile_50 = arcade.Sprite("tile_50.png", 0.5)
        tile_50.center_x = 270
        tile_50.center_y = 780
        tile_50.draw()



    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        self.draw_island01()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()