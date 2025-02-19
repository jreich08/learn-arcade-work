import arcade

arcade.open_window(2000,2000)

arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()

arcade.draw_circle_filled(110,350,30, arcade.csscolor.LIGHT_GREEN)
arcade.finish_render()



arcade.run()

