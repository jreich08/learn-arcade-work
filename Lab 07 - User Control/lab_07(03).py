""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED=5

class Vehicle:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color
        self.width = width
        self.height = height
        arcade.draw_xywh_rectangle_filled(0,130,30, 20, arcade.csscolor.RED)

        self.change_x = 0
        self.change_y = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
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

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def background_image(self):

            # Draw the ground
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.DARK_GREEN)
        #Road Through the forest drawing
        arcade.draw_xywh_rectangle_filled(0, 130, 800, 50, arcade.csscolor.DARK_GRAY)
        arcade.draw_xywh_rectangle_filled(0, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(50, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(100, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(150, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(200, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(250, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(300, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(350, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(400, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(450, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(500, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(550, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(600, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(650, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(700, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(750, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(800, 150, 15, 10, arcade.csscolor.YELLOW)
        arcade.draw_xywh_rectangle_filled(795, 150, 15, 10, arcade.csscolor.YELLOW)

            # Pine Tree
        arcade.draw_xywh_rectangle_filled(420, 200, 20, 71, arcade.csscolor.SIENNA)
        arcade.draw_triangle_filled(390, 220, 470, 220, 430, 240, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(395, 230, 465, 230, 430, 255, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(400, 240, 460, 240, 430, 270, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(405, 240, 455, 240, 430, 285, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(410, 240, 450, 240, 430, 300, arcade.csscolor.LIGHT_GREEN)
            # Pine Tree 2
        arcade.draw_xywh_rectangle_filled(320, 200, 20, 71, arcade.csscolor.SIENNA)
        arcade.draw_triangle_filled(290, 220, 370, 220, 330, 240, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(295, 230, 365, 230, 330, 255, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(300, 240, 360, 240, 330, 270, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(305, 240, 355, 240, 330, 285, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(310, 240, 350, 240, 330, 300, arcade.csscolor.LIGHT_GREEN)
            # Pine Tree 3
        arcade.draw_xywh_rectangle_filled(220, 100, 20, 71, arcade.csscolor.SIENNA)
        arcade.draw_triangle_filled(190, 120, 270, 120, 230, 140, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(195, 130, 265, 130, 230, 155, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(200, 140, 260, 140, 230, 170, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(205, 140, 255, 140, 230, 185, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(210, 140, 250, 140, 230, 200, arcade.csscolor.LIGHT_GREEN)
            # Pine Tree 4
        arcade.draw_xywh_rectangle_filled(420, 100, 20, 71, arcade.csscolor.SIENNA)
        arcade.draw_triangle_filled(390, 120, 470, 120, 430, 140, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(395, 130, 465, 130, 430, 155, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(400, 140, 460, 140, 430, 170, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(405, 140, 455, 140, 430, 185, arcade.csscolor.LIGHT_GREEN)
        arcade.draw_triangle_filled(410, 140, 450, 140, 430, 200, arcade.csscolor.LIGHT_GREEN)

        self.car = Vehicle(0,130,30, 20)
        self.car.position_x

    def on_draw(self):
        arcade.start_render()
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

    def on_draw(self):
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        arcade.start_render()
        self.background_image()


def main():
    window = MyGame()
    arcade.run()

#Create a class for vehicles
#Create a class for something else to be controlled by the mouse
#Chapter 18
#Chapter 19
#self.Car.x


main()