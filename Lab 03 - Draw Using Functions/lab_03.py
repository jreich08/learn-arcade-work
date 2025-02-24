import arcade
from arcade.examples.array_backed_grid import SCREEN_HEIGHT
from arcade.examples.perf_test.stress_test_collision_arcade import SCREEN_WIDTH


# This function opens the arcade window
def main():

    # import the "arcade" library
    arcade.open_window(width=1580, height=1200, window_title="Mini Animation")
    # This defines the size of the drawing window

    # Set Background
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)

def draw_grass():
     # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.DARK_GREEN)

    arcade.start_render()

    arcade.finish_render()
    #Essentially Finishes the Image

    arcade.run()


# This code makes the window stay open



# Calls the Function that opens the drawing window
main()
draw_grass()
