import arcade

# This function opens the arcade window
def main():

    # import the "arcade" library
    arcade.open_window(width=1580, height=1200, window_title="Mini Animation")
    # This defines the size of the drawing window

    # Set Background
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)
    arcade.start_render()

    arcade.finish_render()
    #Essentially Finishes the Image



    arcade.run()
    # This code makes the window stay open

# Calls the Function that opens the drawing window
main()
