import arcade

#player does not have collisions
#pizzas do not exist yet
#money does not exist yet
#rent does not exist yet
#sound does not exist yet
#no second level
#draw car behind the houses so draw the car first
# game assets from here: https://kenney.nl/assets/pico-8-city
#Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Pizza Dash"
TILE_SCALING = 3.0
MAP_FILE = "mapcity.json"
PLAYER_SCALING = 3.0
ENTER_DISTANCE = 80
MONEY_COUNT = 0
RENT_COST = 150


# Creates a class for the car sprite that the player will control
class Car:
    # Int for car class
    def __init__(self, x, y, scaling):
        self.offset = 8 * scaling
        self.scaling = scaling
        self.direction = "east"
        self.speed = 1
        self.physics_engine = None
        #This is when the car is heading East or West

        # Front of car
        self.front = arcade.Sprite()
        self.front.textures = [
            arcade.load_texture("car_front.png"), #Facing East
            arcade.load_texture("car_front.png", mirrored=True), #Facing West
            arcade.load_texture("car_front_upward.png"),  # Facing North/south

            ]


        self.front.texture = self.front.textures[0] #default to east facing
        self.front.scale = scaling
        self.front.center_x = x
        self.front.center_y = y


        # Back of car
        self.back = arcade.Sprite()
        self.back.textures = [
            arcade.load_texture("car_back.png"), #Facing west
            arcade.load_texture("car_back.png", mirrored=True), #Facing East
            arcade.load_texture("car_back_upward.png"), # Facing South

        ]

        self.back.texture = self.back.textures[0]
        self.back.scale = scaling



        self.update_back_position()


    # Update the cars movement and check for collisions
    def update(self):
        # Updates the front of the car
        self.front.update()
        #Updates the back of the car
        self.update_back_position()
        if self.physics_engine:
            self.physics_engine.update()
    #Aligns the back half of the car with the front since it is two pieces
    def update_back_position(self):
        self.front.angle = 0
        self.back.angle = 0
        if self.direction == "east":
            self.front.texture = self.front.textures[0]
            self.back.texture = self.back.textures[0]
            self.back.center_x = self.front.center_x - self.offset
            self.back.center_y = self.front.center_y

        elif self.direction == "west":
            # When heading west the car will now look normal by mirroring
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
            self.front.texture = self.front.textures[2]
            self.back.texture = self.back.textures[2]
            self.front.angle = 180
            self.back.angle = 180
            self.back.center_x = self.front.center_x
            self.back.center_y = self.front.center_y + self.offset


    #Movement controls for each direction
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
    #Stopping movement
    def stop_x(self):
        self.front.change_x = 0

    def stop_y(self):
        self.front.change_y = 0
# Class Establishing My Pizzas
#class Pizza(arcade.sprite):
    #def __init__(self):
        #super().__init__("pizzaiswear.png", scale=0.5)
       # self.center_x = x
        #self.center_y = y
        #self.being_carried = False

#THIS IS BROKEN


# Main Class for the Game Window
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None
        self.scene = None
        #Sprites that the player will be interacting with
        self.car = None
        self.person_sprite = None
        #will be relevant once I code the player getting in and out of the car
        self.in_car = True

        self.physics_engine = None
        #PIZZA CODE
        self.pizza_store = arcade.SpriteList()
        self.delivery_locations = []
        self.active_pizza = None

    def setup(self):
        #boots up the map
        self.tile_map = arcade.load_tilemap(MAP_FILE, scaling=TILE_SCALING)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Car object
        self.car = Car(x=250, y=150, scaling=PLAYER_SCALING)
        self.scene.add_sprite("CarFront", self.car.front)
        self.scene.add_sprite("CarBack", self.car.back)

        # Person sprite it is hidden at first
        self.person_sprite = arcade.Sprite("person.png", PLAYER_SCALING)
        self.person_sprite.center_x = 100
        self.person_sprite.center_y = 100
        self.person_sprite.visible = False
        self.scene.add_sprite("Person", self.person_sprite)
        # Sets the invisible layer in tiled as barrier set. The goal of this is to force the car onto the road
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.car.front,
            walls=self.scene["Barrier"]
        )
        self.car.physics_engine = self.physics_engine
        # Creates and invisible pickup spot unfinished does not actually create a pizza yet
        store_layer = self.tile_map.object_lists.get("Pizza Store", [])
        for obj in store_layer:
            store_point = arcade.Sprite(center_x=obj.shape[0][0], center_y=obj.shape[0][1])
            store_point.visible = False
            self.pizza_store.append(store_point)

        #Pizza Code
            pizza = Pizza(x=obj.shape[0][0], y = obj.shape[0][1])
            self.scene.add_sprite("Pizza", pizza)
            self.active_pizza = pizza



    def on_draw(self):
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time):
       #Updates the cars and physics
        if self.in_car:
            self.car.update()
        else:
            self.person_sprite.update()

        if self.active_pizza and self.active_pizza.being_carried:
                if self.in_car:
                        self.active_pizza.center_x = self.car.front.center_x
                        self.active_pizza.center_y = self.car.front.center_y + 20
                else:
                        self.active_pizza.center_x = self.person_sprite.center_x
                        self.active_pizza.center_y = self.person_sprite.center_y + 20
    #WASD Movement coded
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
            elif key == arcade.key.E:
                # Exit car and makes the player sprite spawn
                self.person_sprite.center_x = self.car.front.center_x - 5
                self.person_sprite.center_y = self.car.front.center_y + 25
                self.person_sprite.visible = True
                self.in_car = False
                print("Exited car")

        else: #player movement code
                if key == arcade.key.W:
                    self.person_sprite.change_y = self.car.speed
                elif key == arcade.key.S:
                    self.person_sprite.change_y = -self.car.speed
                elif key == arcade.key.A:
                    self.person_sprite.change_x = -self.car.speed
                elif key == arcade.key.D:
                    self.person_sprite.change_x = self.car.speed
                elif key == arcade.key.E:
                    distance = arcade.get_distance_between_sprites(self.person_sprite, self.car.front)
                    if distance < 10:
                        self.in_car = True
                        self.person_sprite.visible = False
                        print("Entered car")
                    elif key == arcade.key.E:
                        distance = arcade.get_distance_between_sprites(self.person_sprite, self.active_pizza)
                        if distance < 5:
                            self.being_carried = True
                            print("Picked up a Pizza!")






        if key == arcade.key.ESCAPE:
            arcade.close_window()
    #Stops movement
    def on_key_release(self, key, modifiers):
        if self.in_car:
            if key in [arcade.key.A, arcade.key.D]:
                self.car.stop_x()
            elif key in [arcade.key.W, arcade.key.S]:
                self.car.stop_y()

        else:
            if key in [arcade.key.W, arcade.key.S]:
                self.person_sprite.change_y = 0
            elif key in [arcade.key.A, arcade.key.D]:
                self.person_sprite.change_x = 0
#Launches the game
if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()
