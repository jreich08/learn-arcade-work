import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

class Vehicle:
    def __init__(self, position_x, position_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.color = color

        # Movement deltas (change in x and y)
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        """ Draw the vehicle (a rectangle) """
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)

    def update(self):
        """ Update the position of the vehicle """
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Keep the car within screen boundaries
        if self.position_x < 0:
            self.position_x = 0
        if self.position_x > SCREEN_WIDTH - self.width:
            self.position_x = SCREEN_WIDTH - self.width
        if self.position_y < 0:
            self.position_y = 0
        if self.position_y > SCREEN_HEIGHT - self.height:
            self.position_y = SCREEN_HEIGHT - self.height

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.car = Vehicle(100, 130, 30, 20, arcade.color.RED)

    def background_image(self):
        # This part remains unchanged, it draws the background
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.DARK_GREEN)
        arcade.draw_xywh_rectangle_filled(0, 130, 800, 50, arcade.csscolor.DARK_GRAY)
        arcade.draw_xywh_rectangle_filled(0, 150, 15, 10, arcade.csscolor.YELLOW)
        # (Other background details omitted for brevity)

    def on_draw(self):
        arcade.start_render()
        self.background_image()
        self.car.draw()

    def update(self, delta_time):
        self.car.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.car.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.car.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.car.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.car.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.car.change_x = 0
        if key in (arcade.key.UP, arcade.key.DOWN):
            self.car.change_y = 0


def main():
    window = MyGame()
    arcade.run()

main()