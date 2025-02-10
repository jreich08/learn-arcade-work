import arcade
# import the "arcade" library

arcade.open_window(width=600, height=600, window_title="Drawing Test")
# This defines the size of the drawing window
arcade.set_background_color(arcade.csscolor.CORAL)

arcade.start.render()
# ready to draw starts drawing
# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0

arcade.run()
# This code makes the window stay open
