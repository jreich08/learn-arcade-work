""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 2000


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Iceberg Dodge")

        self.player_list = None

        self.player_sprite = None






    def setup(self):

        #Sprite Lists
        self.player.list = arcade.SpriteList()
        #self.coin_list = arcade.SpriteList()

        #Score
        self.score = 0

        #Set Up The Player
        self.player_sprite = arcade.Sprite("ship-ocean-liner.fbx", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)


    def on_draw(self):
        arcade.start_render()

        #self.coin_list.draw()
        if self.player_list:
            self.player_list.draw()



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()



if __name__ == "__main__":
    main()