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



    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


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