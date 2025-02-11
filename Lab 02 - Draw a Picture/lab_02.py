import arcade
# import the "arcade" library
arcade.open_window(width=600, height=600, window_title="Drawing Test")
# This defines the size of the drawing window
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,600,300,0,arcade.csscolor.DARK_GREEN)
# ready to draw starts drawing
# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_xywh_rectangle_filled(100,300,20,60,arcade.csscolor.SIENNA)
arcade.draw_circle_filled(110,350,30, arcade.csscolor.LIGHT_GREEN)
arcade.draw_xywh_rectangle_filled(180,300,20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(190, 370,60, 80, arcade.csscolor.LIGHT_GREEN )
arcade.draw_xywh_rectangle_filled(280,300, 20,75,arcade.csscolor.SIENNA)
arcade.draw_arc_filled(280, 350, 20, 100, start_angle=100,end_angle=180,tilt_angle=450, color=arcade.csscolor.LIGHT_GREEN)
arcade.draw_arc_filled(290, 350, 20, 100, start_angle=100,end_angle=180,tilt_angle=-130, color=arcade.csscolor.LIGHT_GREEN)
arcade.draw_xywh_rectangle_filled(420, 300, 20, 90, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 320, 460, 320, 440, 340 ,arcade.csscolor.LIGHT_GREEN)

arcade.finish_render()
arcade.run()
# This code makes the window stay open
#make sure to add more comments