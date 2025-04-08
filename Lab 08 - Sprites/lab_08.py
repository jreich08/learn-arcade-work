""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50
OBSTACLE_COUNT = 15

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0


        self.coin_sound = arcade.load_sound(":resources:sounds/coin3.wav")


    def update(self, delta_time: float = 1 / 60) -> None:

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class Obstacle(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

        # Sound effect for hitting an obstacle
        self.hit_sound = arcade.load_sound(":resources:sounds/hurt3.wav")

    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Iceberg Dodge")

        self.player_list = None

        self.player_sprite = None

        self.coin_list = None

        self.obstacle_list = None


        self.set_mouse_visible(False)

        self.game_over = False

        self.game_won = False

        self.sound_player = None



    def setup(self):
        # Sprite Lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set Up The Player
        self.player_sprite = arcade.Sprite("ship (7).png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randint(0, SCREEN_WIDTH)
            coin.center_y = random.randint(0, SCREEN_HEIGHT)
            coin.change_x = random.choice([-1, 1]) * random.uniform(1, 3)
            coin.change_y = random.choice([-1, 1]) * random.uniform(1, 3)
            self.coin_list.append(coin)

        self.obstacle_list = arcade.SpriteList()

        for i in range(OBSTACLE_COUNT):
            #Imagine these are icebergs...
            obstacle = Obstacle(":resources:images/space_shooter/meteorGrey_big2.png", 0.5)
            obstacle.center_x = random.randint(100, SCREEN_WIDTH - 100)
            obstacle.center_y = random.randint(100, SCREEN_HEIGHT - 100)
            obstacle.change_x = random.choice([-1, 1]) * random.uniform(1, 2)
            obstacle.change_y = random.choice([-1, 1]) * random.uniform(1, 2)
            self.obstacle_list.append(obstacle)

        #I got inspired and added some music I found for free online
        #I linked where I got it in the next line, but I named the filed "MUSIC.mp3" after download
        #https://www.fesliyanstudios.com/royalty-free-music/download/8-bit-menu/287 I downloaded the slower one
        self.background_music = arcade.load_sound("MUSIC.mp3")
        arcade.play_sound(self.background_music)


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


        self.coin_list.draw()
        if self.player_list:
            self.player_list.draw()

        self.coin_list.draw()
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 100, arcade.color.WHITE, 14)

        self.obstacle_list.draw()

        if self.game_over:
            arcade.draw_text("GAME OVER", (SCREEN_WIDTH /3), SCREEN_HEIGHT / 2,
                             arcade.color.RED, 36)

        if self.game_won:
            arcade.draw_text("GAME WON CONGRATS!!!", (SCREEN_WIDTH / 2.5) - 200, SCREEN_HEIGHT / 2, arcade.color.GREEN,
                             36)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):

        """ Movement and game logic """
        self.player_list.update()

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()

        # Generate a list of all sprites that collided with the player.
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            #print("Playing sound") ( just put this in bc I didnt want to annoy everyone around me)
            if not self.sound_player or not self.sound_player.playing:
                self.sound_player = arcade.play_sound(coin.coin_sound)

        self.obstacle_list.update()

        if self.score < 25:

            obstacle_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_list)
            if obstacle_hit_list:
                for obstacle in obstacle_hit_list:
                    if len(self.coin_list) > 25:
                        obstacle.remove_from_sprite_lists()
                self.score -= 1
                if not self.sound_player or not self.sound_player.playing:
                    self.sound_player = arcade.play_sound(obstacle.hit_sound)
                if len(self.coin_list) < 0:
                    self.game_over = True




        if self.score < 0:
            self.game_over = True

        if self.score > 25:
            self.game_won = True


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()



if __name__ == "__main__":
    main()


