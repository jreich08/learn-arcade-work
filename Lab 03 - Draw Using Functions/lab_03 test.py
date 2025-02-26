import arcade
car_x=100
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
def draw_grass():
    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.DARK_GREEN)

def green_tree(x, y):
    #This function will draw a green Tree
    # use x = 430, y = 240 as the position to determine the expressions for the
    # parameters of the drawing functions below
    arcade.draw_xywh_rectangle_filled(x - 8, y - 40, 15, 71, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(x, 40 + y, 30, arcade.color.LIGHT_GREEN)


    # Draw a point at x,y for reference
    #arcade.draw_point(x, y, arcade.color.RED, 5)
#This function will draw a road through the forest
def road_draw(x,y):
    arcade.draw_xywh_rectangle_filled(0, 130, 800,50, arcade.csscolor.DARK_GRAY)

#This Function Will Draw a Car to drive down the road

def draw_stripes(x,y):
    arcade.draw_xywh_rectangle_filled(x - 50, y - 150, 15, 10, arcade.csscolor.YELLOW)

def draw_car(x,y):
    arcade.draw_xywh_rectangle_filled(x, y - 130 , 30, 20, arcade.csscolor.RED)

    #draw_car(100,130)


def on_draw(delta_time):
    global car_x
    arcade.start_render()

    draw_grass()
#Draws the road
    road_draw(100,130)

    draw_stripes(50,300)
    draw_stripes(100,300)
    draw_stripes(150, 300)
    draw_stripes(200, 300)
    draw_stripes(250,300)
    draw_stripes(300, 300)
    draw_stripes(350, 300)
    draw_stripes(400, 300)
    draw_stripes(450, 300)
    draw_stripes(500, 300)
    draw_stripes(550, 300)
    draw_stripes(600, 300)
    draw_stripes(650, 300)
    draw_stripes(700, 300)
    draw_stripes(750, 300)
    draw_stripes(800, 300)

    draw_car(car_x, 260)

    car_x += 1

#Draw a green tree

    green_tree(100,100)
    green_tree(300,70)
    green_tree(400,90)
    green_tree(600,150)
    green_tree(700,60)
    green_tree(200,55)
    green_tree(50,230)
    green_tree(800,100)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)



    #  Finish and run
    #arcade.finish_render()
    # Call on draw every 60th of a second
    arcade.schedule(on_draw, 1/60)

    arcade.run()

# Call The Main Function to Get the Program Started
main()
