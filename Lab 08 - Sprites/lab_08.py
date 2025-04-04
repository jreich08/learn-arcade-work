""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

class Coin(arcade.Sprite):

    def update(self):
        self.angle += self.change_angle

        self.center_y -= 1

        if self.center_y == 0:
            self.center_y = SCREEN_HEIGHT


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Iceberg Dodge")

        self.player_list = None

        self.player_sprite = None

        self.set_mouse_visible(False)






    def setup(self):

        #Sprite Lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        #Score
        self.score = 0

        #Set Up The Player
        #Ship file https://kenney.nl/assets/pirate-pack
        self.player_sprite = arcade.Sprite("ship (7).png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)


        for i in range(COIN_COUNT):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)



    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


        #self.coin_list.draw()
        if self.player_list:
            self.player_list.draw()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    #def on_update(self, delta_time):





def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()



if __name__ == "__main__":
    main()


#Need a bad class