import arcade
import random


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
 #Class Establishing My Pizzas
class Pizza(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("pizzaiswear.png", scale=2.0)
        self.center_x = x
        self.center_y = y
        self.being_carried = False




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
        self.in_car = False

        self.physics_engine = None
        #PIZZA CODE
        self.pizza_store = arcade.SpriteList()
        self.delivery_locations = []
        self.active_pizza = None
        self.money = 0
        self.time_left = 5
        self.time_left = 110
        self.game_over = False
        self.eviction_notice = None
        self.game_state = "START"


    def setup(self):
        # boots up the map
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
        self.person_sprite.center_x = 250
        self.person_sprite.center_y = 175
        self.person_sprite.visible = True
        self.scene.add_sprite("Person", self.person_sprite)
        #Flag Sprite
        """FLAG"""
        self.delivery_icon = arcade.Sprite(":resources:images/items/flagGreen2.png", scale=0.15)
        self.delivery_icon.visible = False
        self.scene.add_sprite("DeliveryIcon", self.delivery_icon)
        self.current_target = None

        # Sets the invisible layer in tiled as barrier set. The goal of this is to force the car onto the road
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.car.front,
            walls=self.scene["Barrier"]
        )
        self.car.physics_engine = self.physics_engine

        # Creates an invisible pickup spot — unfinished — does not actually create a pizza yet
        # PIZZA CODE
        store_layer = self.tile_map.object_lists.get("PizzaStore", [])
        if not store_layer:
            print(" No pizza spawn objects found in 'PizzaStore' layer.")
        else:
            for obj in store_layer:
                try:
                    x, y = obj.shape
                    print(f" Pizza spawn point: ({x}, {y})")

                    store_point = arcade.Sprite(center_x=x, center_y=y)
                    store_point.visible = False
                    self.pizza_store.append(store_point)

                    pizza = Pizza(x, y)
                    self.scene.add_sprite("pizzaiswear.png", pizza)
                    self.active_pizza = pizza
                    print(" Pizza created and added to scene.")
                except Exception as e:
                    print(" handling pizza object problem", e)

            self.store_layer_data = store_layer

        # DELIVERY POINTS LOADING
        delivery_layer = self.tile_map.object_lists.get("DeliveryPoints", [])
        manual_delivery_coords = [
            (35.0, 74.0),
            (180.0, 196.0),
            (299.0, 174.0),
            (349.0, 314.0),
            (418.0, 172.0),
            (177.0, 54.0)
        ]

        for coord in manual_delivery_coords:
            delivery_point = arcade.Sprite(center_x=coord[0], center_y=coord[1])
            delivery_point.visible = False
            self.delivery_locations.append(delivery_point)
            print(f" Delivery point added at {coord}")

        if self.delivery_locations:
            self.current_target = random.choice(self.delivery_locations)
            self.delivery_icon.center_x = self.current_target.center_x
            self.delivery_icon.center_y = self.current_target.center_y
            self.delivery_icon.visible = True
            print("Delivery target set and flag placed.")

        self.eviction_image = arcade.Sprite("eviction_notice.png", scale=0.6)
        self.eviction_image.center_x = SCREEN_WIDTH // 2
        self.eviction_image.center_y = SCREEN_HEIGHT // 2
        self.eviction_image.visible = False
        self.scene.add_sprite("UI", self.eviction_image)


        # Music for the game found here https://pixabay.com/music/synth-pop-global-djs-part-five-italo-style-5038/
        self.background_music = arcade.load_sound("pizzamusic.wav")
        self.background_music_player = self.background_music.play(volume=0.5, loop=True)

        # picup sound link https://pixabay.com/sound-effects/coin-collect-retro-8-bit-sound-effect-145251/
        self.pickup_sound = arcade.load_sound("coin-collect-retro-8-bit-sound-effect-145251.wav")

        # Car door noise link https://pixabay.com/sound-effects/car-door-47981/
        self.enter_exit_sound = arcade.load_sound("car-door-47981.wav")
        # Car engine noise https://pixabay.com/sound-effects/car-engine-noise-321224/
        self.car_idle_sound = arcade.load_sound("car-engine-noise-321224.wav")
        self.car_idle_player = None
        #GOT THIS FROM HERE https://pixabay.com/sound-effects/cash-register-purchase-87313/
        self.delivery_sound = arcade.load_sound("cash-register-purchase-87313.wav")
        #Got this from here https://pixabay.com/sound-effects/level-failed-80951/
        self.game_fail_sound = arcade.load_sound("level-failed-80951.wav")
        #got this from here https://pixabay.com/sound-effects/you-win-sequence-3-183950/
        self.game_win_sound = arcade.load_sound("you-win-sequence-3-183950.wav")

    def handle_pizza_delivery(self):
        print("Pizza Delivered!")
        arcade.play_sound(self.delivery_sound, volume=3.0)
        self.money += 25
        self.active_pizza.remove_from_sprite_lists()
        self.active_pizza = None
        self.delivery_icon.visible = False

        # Spawn new pizza
        if self.store_layer_data:
            spawn_obj = random.choice(self.store_layer_data)
            x, y = spawn_obj.shape
            new_pizza = Pizza(x, y)
            self.scene.add_sprite("Pizza", new_pizza)
            self.active_pizza = new_pizza
            print("New pizza spawned!")

        # Set new delivery target
        if self.delivery_locations:
            self.current_target = random.choice(self.delivery_locations)
            self.delivery_icon.center_x = self.current_target.center_x
            self.delivery_icon.center_y = self.current_target.center_y
            self.delivery_icon.visible = True
            print("New delivery target set!")

        if self.money >= RENT_COST:
            self.game_state = "WIN"
            self.delivery_icon.visible = False
            if self.background_music_player:
                self.background_music_player.pause()
            arcade.play_sound(self.game_win_sound, volume =2  )
            print("You Win!")

    def on_draw(self):
        self.clear()
        if self.game_state == "START":
            arcade.draw_text("WELCOME TO PIZZA DASH!", 100, 350, arcade.color.BLACK, 24, font_name = "Kenny Mini")
            arcade.draw_text("Use WASD to move", 100, 310, arcade.color.DARK_BLUE, 18, font_name = "Kenny Mini")
            arcade.draw_text("Press E to get in/out of the car or pick up pizza", 100, 280, arcade.color.DARK_BLUE, 18, font_name = "Kenny Mini")
            arcade.draw_text("Deliver the pizza to the green flag!", 100, 250, arcade.color.DARK_BLUE, 18, font_name = "Kenny Mini")
            arcade.draw_text("Press ENTER to Start", 100, 180, arcade.color.RED, 20, font_name = "Kenny Mini")
            arcade.draw_text("Collect $150 from deliveries before the timer runs out!", 100, 220, arcade.color.DARK_BLUE, 18, font_name = "Kenny Mini")
        elif self.game_state == "PLAYING":
            self.scene.draw()
            arcade.draw_text(f"Money: ${self.money}", 570, SCREEN_HEIGHT - 20, arcade.color.BLACK, 14,
                             font_name="Kenney Mini") #from arcade library
            arcade.draw_text(f"Time Left: {int(self.time_left)}s", 570, SCREEN_HEIGHT - 40, arcade.color.BLACK, 14,
                             font_name="Kenney Mini")

        elif self.game_state == "WIN":
            if self.car_idle_player and self.car_idle_player.playing:
                self.car_idle_player.pause()
                self.car_idle_player = None
            arcade.draw_text("YOU WIN!", 210, 300, arcade.color.GREEN, 32, bold=True)
            arcade.draw_text(f"Final Earnings: ${self.money}", 220, 250, arcade.color.GREEN, 20)
            arcade.draw_text("Press ESC to Quit", 220, 180, arcade.color.GRAY, 18)

    def on_update(self, delta_time):
        if self.game_state != "PLAYING":
            return

        if self.game_over:
            return

        # Updates the cars and physics
        if self.in_car:
            self.car.update()
        else:
            self.person_sprite.update()

        # Carry pizza with player or car
        if self.active_pizza and self.active_pizza.being_carried:
            if self.in_car:
                self.active_pizza.center_x = self.car.front.center_x
                self.active_pizza.center_y = self.car.front.center_y + 20
            else:
                self.active_pizza.center_x = self.person_sprite.center_x
                self.active_pizza.center_y = self.person_sprite.center_y + 20



        # Timer update
        self.time_left -= delta_time
        if self.time_left <= 0:
            print("Time's up!")
            self.time_left = 0

            if self.time_left <= 0 and not self.game_over:
                self.time_left = 0
                if self.money < RENT_COST:
                    print("Evicted! You couldn't pay the rent.")
                    self.eviction_image.visible = True
                    if self.car_idle_player and self.car_idle_player.playing:
                        self.car_idle_player.pause()
                        self.car_idle_player = None
                    if self.background_music_player:
                        self.background_music_player.pause()
                    arcade.play_sound(self.game_fail_sound,1)
                    self.game_over = True

            if self.game_state == "WIN":
                return


            """PIZZA GENERATION AREA"""
            # DELIVERY CHECK AND PIZZA REGENERATION
            if self.active_pizza and self.active_pizza.being_carried:
                for point in self.delivery_locations:
                    if self.current_target and arcade.get_distance_between_sprites(self.active_pizza, self.current_target) < 20:
                        print("Pizza Delivered!")
                        arcade.play_sound(self.delivery_sound, volume=1.0)
                        self.money += 25
                        self.active_pizza.remove_from_sprite_lists()
                        self.active_pizza = None
                        self.delivery_icon.visible = False


                        if self.delivery_locations:
                            self.current_target = random.choice(self.delivery_locations)
                            self.delivery_icon.center_x = self.current_target.center_x
                            self.delivery_icon.center_y = self.current_target.center_y
                            self.delivery_icon.visible = True

                        if self.delivery_locations:
                            self.current_target = random.choice(self.delivery_locations)
                            self.delivery_icon.center_x = self.current_target.center_x
                            self.delivery_icon.center_y = self.current_target.center_y
                            self.delivery_icon.visible = True
                            print("New target selected!")

                        # Generate new pizza at random store point
                        if self.store_layer_data:
                            spawn_obj = random.choice(self.store_layer_data)
                            x, y = spawn_obj.shape
                            new_pizza = Pizza(x, y)
                            self.scene.add_sprite("Pizza", new_pizza)
                            self.active_pizza = new_pizza
                            print("New pizza spawned!")

                            if self.delivery_locations:
                                self.current_target = random.choice(self.delivery_locations)
                                self.delivery_icon.center_x = self.current_target.center_x
                                self.delivery_icon.center_y = self.current_target.center_y
                                self.delivery_icon.visible = True

                                if not self.active_pizza or not self.active_pizza.being_carried:
                                    self.delivery_icon.visible = False

    #WASD Movement coded
    def on_key_press(self, key, modifiers):
        if self.game_over:
            return

        if self.game_state == "START" and key == arcade.key.ENTER:
            self.game_state = "PLAYING"
            print("Game started!")
            return
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
                if self.active_pizza and self.active_pizza.being_carried:
                    self.active_pizza.visible = True
                if self.car_idle_player and self.car_idle_player.playing:
                    self.car_idle_player.pause()
                    self.car_idle_player = None
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
                        if self.active_pizza and self.active_pizza.being_carried:
                            self.active_pizza.visible = False
                        arcade.play_sound(self.enter_exit_sound, volume = 2)
                        if self.car_idle_player is None or not self.car_idle_player.playing:
                            self.car_idle_player = self.car_idle_sound.play(volume=0.5)
                            self.car_idle_player.loop = True
                        print("Entered car")
                    elif key == arcade.key.E:
                        # Check if near the car to enter
                        if arcade.get_distance_between_sprites(self.person_sprite, self.car.front) < 10:
                            self.in_car = True
                            self.person_sprite.visible = False
                            if self.active_pizza and self.active_pizza.being_carried:
                                self.active_pizza.visible = False
                            arcade.play_sound(self.enter_exit_sound, volume=2)
                            if self.car_idle_player is None or not self.car_idle_player.playing:
                                self.car_idle_player = self.car_idle_sound.play(volume=0.5)
                                self.car_idle_player.loop = True
                            print("Entered car")

                        # Check if near pizza to pick up
                        elif self.active_pizza and not self.active_pizza.being_carried and \
                                arcade.get_distance_between_sprites(self.person_sprite, self.active_pizza) < 10:
                            self.active_pizza.being_carried = True
                            arcade.play_sound(self.pickup_sound, volume=2)
                            print("Picked up a Pizza!")

                        # Check if near delivery point to deliver
                        elif self.active_pizza and self.active_pizza.being_carried and \
                                arcade.get_distance_between_sprites(self.person_sprite, self.current_target) < 20:
                            print("Attempting delivery")
                            self.handle_pizza_delivery()








        if key == arcade.key.ESCAPE:
            arcade.close_window()
    #Stops movement
    def on_key_release(self, key, modifiers):
        if self.game_over:
            return
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

#wat