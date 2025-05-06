import arcade
#Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Pizza Dash"
TILE_SCALING = 3.0
MAP_FILE = "mapcity.json"
PLAYER_SCALING = 3.0
ENTER_DISTANCE = 80
#Creates a class for the car sprite that the player will control
class Car:
    # Int for car class
    def __init__(self, x, y, scaling):
        self.offset = 8 * scaling
        self.scaling = scaling
        self.direction = "east"
        self.speed = 1
        self.physics_engine = None

        # Front of car
        self.front = arcade.Sprite()
        self.front.textures = [
            arcade.load_texture("car_front.png"),                    # 0: east
            arcade.load_texture("car_front.png", mirrored=True),     # 1: west
            arcade.load_texture("car_front_upward.png")              # 2: north/south
        ]
        self.front.texture = self.front.textures[0]
        self.front.scale = scaling
        self.front.center_x = x
        self.front.center_y = y

        # Back of car
        self.back = arcade.Sprite()
        self.back.textures = [
            arcade.load_texture("car_back.png"),                     # 0: east
            arcade.load_texture("car_back.png", mirrored=True),      # 1: west
            arcade.load_texture("car_back_upward.png")               # 2: north/south
        ]
        self.back.texture = self.back.textures[0]
        self.back.scale = scaling

        self.update_back_position()

    # Update the cars movement and check for collisions
    def update(self):
        self.front.update()
        self.update_back_position()
        if self.physics_engine:
            self.physics_engine.update()

    def update_back_position(self):
        if self.direction == "east":
            self.front.angle = 0
            self.back.angle = 0
            self.front.texture = self.front.textures[0]
            self.back.texture = self.back.textures[0]
            self.back.center_x = self.front.center_x - self.offset
            self.back.center_y = self.front.center_y

        elif self.direction == "west":
            self.front.angle = 0
            self.back.angle = 0
            self.front.texture = self.front.textures[1]
            self.back.texture = self.back.textures[1]
            self.back.center_x = self.front.center_x + self.offset
            self.back.center_y = self.front.center_y

        elif self.direction == "north":
            self.front.angle = 0
            self.back.angle = 0
            self.front.texture = self.front.textures[2]
            self.back.texture = self.back.textures[2]
            self.back.center_x = self.front.center_x
            self.back.center_y = self.front.center_y - self.offset

        elif self.direction == "south":
            self.front.angle = 180
            self.back.angle = 180
            self.front.texture = self.front.textures[2]  # reuse upward sprite
            self.back.texture = self.back.textures[2]    # reuse upward sprite
            self.back.center_x = self.front.center_x
            self.back.center_y = self.front.center_y + self.offset

    def move_left(self):
        self.front.change_x = -self.speed
        self.direction = "west"

    def move_right(self):
        self.front.change_x = self.speed
        self.direction = "east"

    def move_up(self):
        self.front.change_y = self.speed
        self.direction = "north"

    def move_down(self):
        self.front.change_y = -self.speed
        self.direction = "south"

    def stop_x(self):
        self.front.change_x = 0

    def stop_y(self):
        self.front.change_y = 0

# Main Class for the Game Window
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None
        self.scene = None
        self.car = None
        self.person_sprite = None
        self.in_car = True
        self.physics_engine = None

    def setup(self):
        self.tile_map = arcade.load_tilemap(MAP_FILE, scaling=TILE_SCALING)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.car = Car(x=250, y=150, scaling=PLAYER_SCALING)
        self.scene.add_sprite("CarFront", self.car.front)
        self.scene.add_sprite("CarBack", self.car.back)

        self.person_sprite = arcade.Sprite("person.png", PLAYER_SCALING)
        self.person_sprite.center_x = 100
        self.person_sprite.center_y = 100
        self.person_sprite.visible = False
        self.scene.add_sprite("Person", self.person_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.car.front,
            walls=self.scene["Barrier"]
        )
        self.car.physics_engine = self.physics_engine

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time):
        if self.in_car:
            self.car.update()

    def on_key_press(self, key, modifiers):
        if self.in_car:
            if key == arcade.key.W:
                self.car.move_up()
            elif key == arcade.key.S:
                self.car.move_down()
            elif key == arcade.key.A:
                self.car.move_left()
            elif key == arcade.key.D:
                self.car.move_right()

        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key, modifiers):
        if self.in_car:
            if key in [arcade.key.A, arcade.key.D]:
                self.car.stop_x()
            elif key in [arcade.key.W, arcade.key.S]:
                self.car.stop_y()

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
