import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
car_x=100
def draw_grass():
    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.DARK_GREEN)

def pine_tree(x, y):
    # Draw a point at x,y for reference
    #arcade.draw_point(x, y, arcade.color.RED, 5)

    #Pine Tree
    arcade.draw_xywh_rectangle_filled(420, 200, 20, 71, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(390, 220, 470, 220, 430, 240, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(395, 230, 465, 230, 430, 255, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(400, 240, 460, 240, 430, 270, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(405, 240, 455, 240, 430, 285, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(410, 240, 450, 240, 430, 300, arcade.csscolor.LIGHT_GREEN)
    #Pine Tree 2
    arcade.draw_xywh_rectangle_filled(320, 200, 20, 71, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(290, 220, 370, 220, 330, 240, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(295, 230, 365, 230, 330, 255, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(300, 240, 360, 240, 330, 270, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(305, 240, 355, 240, 330, 285, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(310, 240, 350, 240, 330, 300, arcade.csscolor.LIGHT_GREEN)
    #Pine Tree 3
    arcade.draw_xywh_rectangle_filled(220, 100, 20, 71, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(190, 120, 270, 120, 230, 140, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(195, 130, 265, 130, 230, 155, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(200, 140, 260, 140, 230, 170, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(205, 140, 255, 140, 230, 185, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(210, 140, 250, 140, 230, 200, arcade.csscolor.LIGHT_GREEN)
    #Pine Tree 4
    arcade.draw_xywh_rectangle_filled(420, 100, 20, 71, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(390, 120, 470, 120, 430, 140, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(395, 130, 465, 130, 430, 155, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(400, 140, 460, 140, 430, 170, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(405, 140, 455, 140, 430, 185, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(410, 140, 450, 140, 430, 200, arcade.csscolor.LIGHT_GREEN)
#This function will draw a road through the forest
def road_draw(x,y):
    arcade.draw_xywh_rectangle_filled(0, 130, 800,50, arcade.csscolor.DARK_GRAY)
    arcade.draw_xywh_rectangle_filled(0, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(50, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(100, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(150, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(200, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(250, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(300, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(350, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(400, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(450, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(500, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(550, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(600, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(650, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(700, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(750, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(800, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(795, 150, 15,10, arcade.csscolor.YELLOW)
#This Function Will Draw a Car to drive down the road
def draw_car(x, y):
    arcade.draw_xywh_rectangle_filled(x, y , 30, 20, arcade.csscolor.RED)


    #draw_car(100,130)


def on_draw(delta_time):
    global car_x
    arcade.start_render()

    draw_grass()
#Draws the road
    road_draw(100,130)

    draw_car(car_x, 130)


    car_x += 1
    #Draws the car
    #draw_car(100,130)

    # Draw a pine tree
    pine_tree(10, 10)


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
