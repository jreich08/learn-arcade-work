import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5
DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Moving With Screen & WALLS!"

VIEWPORT_MARGIN = 220
CAMERA_SPEED = 0.1
PLAYER_MOVEMENT_SPEED = 7

class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0


        self.coin_sound = arcade.load_sound(":resources:sounds/coin3.wav")

    def collect(self, player_sprite):
        if self.collides_with_sprite(player_sprite):
            self.coin_sound.play()


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None
        self.physics_engine = None
        self.score=0
        self.sound_player = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.coin_list = None

        self.camera_sprites = arcade.Camera(width, height)
        self.camera_gui = arcade.Camera(width, height)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/robot/robot_walk6.png", SPRITE_SCALING)
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)
        self.score=0


        level_width = 2000
        level_height = 1600
        tile_size = 64

        # Create border walls
        for x in range(0, level_width, tile_size):
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/grassLeft.png", SPRITE_SCALING, center_x=x, center_y=0))
            self.wall_list.append(arcade.Sprite(":resources:images/tiles/grass.png", SPRITE_SCALING, center_x=x,
                                                center_y=level_height - tile_size))

        for y in range(0, level_height, tile_size):
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING, center_x=0, center_y=y))
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING, center_x=level_width - tile_size,
                              center_y=y))

        for x in range(128, 800, tile_size):
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=x, center_y=512))

        for x in range(900, 1600, tile_size):
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=x, center_y=700))

        for y in range(300, 700, tile_size):
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=600, center_y=y))

        for y in range(300, 1000, tile_size):
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=1300, center_y=y))
        for y in range(600, 1000, 64):
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=400, center_y=y))
        for x in range(400, 700, 64):
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=x, center_y=1000))

        num_coins = 10
        for _ in range(num_coins):
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING)

            while True:
                coin.center_x = random.randint(64, level_width - 64)
                coin.center_y = random.randint(64, level_height - 64)

                if not arcade.check_for_collision_with_list(coin, self.wall_list):
                    break

            self.coin_list.append(coin)


        box_coords = [
            (1200, 1200), (1264, 1200), (1328, 1200),
            (1200, 1264), (1328, 1264),
            (1200, 1328), (1264, 1328), (1328, 1328),

        ]
        for coord in box_coords:
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=coord[0],
                              center_y=coord[1]))

        vertical_wall_coords = [
            (1400, 1400), (1400, 1464), (1400, 1400),
            (1400, 1470), (1400, 1470), (110, 230),(170,230), (230,230), (290,230),
            (290, 1300), (230,1300), (170,1300), (110,1300),
            (500, 1300), (560, 1300), (620, 1300), (680, 1300)

        ]
        for coord in vertical_wall_coords:
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=coord[0],
                              center_y=coord[1]))




        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        maze_coords = [
            (960, 960), (1024, 960), (1088, 960),
            (960, 1024), (960, 1088), (1088, 1024),
            (1024, 1088), (1088, 1088)
        ]
        for x, y in maze_coords:
            self.wall_list.append(
                arcade.Sprite(":resources:images/tiles/stoneMid.png", SPRITE_SCALING, center_x=x, center_y=y))

        self.background_music = arcade.load_sound("pixel-perfect-112527.mp3")
        arcade.play_sound(self.background_music)


        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.camera_sprites.use()
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

        self.camera_gui.use()
        arcade.draw_text("Use arrow keys to move", 10, 100, arcade.color.WHITE, 14)

        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.color.WHITE, 18)

    def on_update(self, delta_time):
        self.physics_engine.update()

        # Movement handling
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            # print("Playing sound")  # just put this in bc I didnt want to annoy everyone around me
            if not self.sound_player or not self.sound_player.playing:
                self.sound_player = arcade.play_sound(coin.coin_sound)


        self.scroll_to_player()

    def scroll_to_player(self):
        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

def main():
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()


